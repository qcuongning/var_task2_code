#!/usr/bin/env python
# coding: utf-8

# In[37]:


get_ipython().system('nvidia-smi')


# In[53]:


type(emb_model)


# In[33]:


import torch
import os
from transformers import Qwen3VLForConditionalGeneration, AutoProcessor
from PIL import Image
from io import BytesIO
from typing import List, Dict, Tuple
import pandas as pd
from tqdm import tqdm
import random
import numpy as np
import pickle as pkl
import re


# In[3]:


def set_seed(seed_value=42):
    """
    Sets the seed for Python, NumPy, and PyTorch/CUDA to ensure reproducibility.
    """
    # 1. Set seed for built-in Python 'random' library
    random.seed(seed_value)
    os.environ['PYTHONHASHSEED'] = str(seed_value)
    
    # 2. Set seed for NumPy
    np.random.seed(seed_value)
    
    # 3. Set seed for PyTorch
    torch.manual_seed(seed_value)
    
    # 4. Set seed for CUDA/GPU operations (crucial for GPU use)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed_value)
        torch.cuda.manual_seed_all(seed_value) # for multi-GPU setup
        
        # Ensures deterministic algorithms are used. This can slightly slow down GPU operations.
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False 
        print(f"Seed {seed_value} set for Python, NumPy, PyTorch, and CUDA.")
    else:
        print(f"Seed {seed_value} set for Python, NumPy, and PyTorch (CPU mode).")

# Example usage:
MY_SEED = 68
set_seed(MY_SEED)


# In[4]:


# --- Configuration ---
# CHANGE THIS: Must be the local path where you saved the Qwen-VL-4B-Instruct model
LOCAL_MODEL_PATH = "./Qwen-VL-4B-Instruct" 
# Ensure you are using the appropriate device (CPU for most local setups, or CUDA for GPU)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
QUESTION_CSV = 'question_with_ans.csv'
# ANS_PATH = '/workspace/VAR2025/OCR/data/ans.txt'


# In[5]:


# --- 1. Simulate Multimodal Retrieval (Offline Indexing) ---
# In a real system, a vector database would return this data.

def create_dummy_image(path: str):
    """Creates a simple black image file for demonstration purposes."""
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # Create a simple 200x200 black image
        img = Image.new('RGB', (200, 200), color = 'black')
        img.save(path)
        print(f"Created dummy image at: {path}")

# Simulated Retrieved Context
RETRIEVED_TEXT = [
    "Context 1: Theo Nghị định 34/2024/NĐ-CP, mục đích chính của việc lắp đặt camera giám sát là để đảm bảo an toàn và theo dõi chất lượng sản phẩm.",
    "Context 2: Hình ảnh dưới đây minh họa một bảng điều khiển trung tâm với nút khẩn cấp (Emergency Stop) màu đỏ.",
    "Context 3: Quy tắc an toàn lao động yêu cầu phải đội mũ bảo hộ tại công trường, được quy định tại Điều 5, mục 2. (Source: ATLD_QuyTac_01)"
]

RETRIEVED_IMAGES_PATHS = [
    "./retrieved_data/image_01.png",  # Example of a relevant image (e.g., safety vest)
    "./retrieved_data/image_02.png",  # Example of an irrelevant image (e.g., random office item)
]

# Create dummy images so the script runs
for p in RETRIEVED_IMAGES_PATHS:
    create_dummy_image(p)

# Multiple-Choice Question (Vietnamese)
QUESTION = "Theo các thông tin được cung cấp, yếu tố nào là **bắt buộc** tại công trường xây dựng? (A) Lắp đặt camera. (B) Nút khẩn cấp màu đỏ. (C) Đội mũ bảo hộ. (D) Áo bảo hộ."

# --- 2. Multimodal Augmentation (Prompt Engineering for Qwen-VL) ---

def augment_prompt_qwen_vl(text_context: List[str], image_paths: List[str], question: str) -> Tuple[str, List[Image.Image]]:
    """
    Constructs the prompt and gathers image objects for Qwen-VL-4B-Instruct.
    """
    
    # 1. Structure Text Context
    context_text = "\n".join([f"({i+1}) {t}" for i, t in enumerate(text_context)])
    
    # 2. Prepare Images
    image_objects = []
    image_placeholders = []
    for i, path in enumerate(image_paths):
        try:
            image_objects.append(Image.open(path).convert('RGB'))
            # Qwen-VL uses the '<image>' token as a placeholder in the text stream
            image_placeholders.append(f"<image>")
        except Exception as e:
            print(f"Error loading image {path}: {e}")

    # 3. Construct the Full Prompt (Vietnamese + Placeholders)
    # The image placeholders are inserted at the beginning of the user message.
    image_prompt = "".join(image_placeholders)
    
    # Combine image placeholders, text context, and question into the user message
    user_message = (
        f"{image_prompt}\n"
        f"Đây là các thông tin và hình ảnh được truy xuất để trả lời câu hỏi của tôi:\n"
        f"--- CONTEXT TRUY XUẤT ---\n"
        f"{context_text}\n"
        f"------------------------\n"
        f"Dựa vào thông tin trên, hãy chọn câu trả lời đúng nhất cho câu hỏi trắc nghiệm tiếng Việt sau: {question}\n"
        f"Chỉ trả lời (A), (B), (C), hoặc (D)."
    )

    # Qwen-VL Instruction Format
    prompt = f"<|im_start|>user\n{user_message}<|im_end|>\n<|im_start|>assistant\n"
    
    return prompt, image_objects

# --- 3. Multimodal Generation (Inference) ---

def run_multimodal_qa(local_path: str, prompt: str, image_objects: List[Image.Image]):
    """Loads the model and generates the answer."""
    
    if not os.path.exists(local_path):
        print(f"Error: Model not found at local path: {local_path}")
        print("Please ensure you have downloaded the Qwen-VL-4B-Instruct weights and saved them correctly.")
        return "ERROR"
        
    try:
        # Load Model and Tokenizer (Offline)
        print("\nLoading Qwen-VL model and tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(local_path, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            local_path,
            device_map=DEVICE, # Use GPU if available
            trust_remote_code=True,
            fp16=True # Use half-precision for lower memory usage
        ).eval()

        # Tokenize and Process Input
        inputs = tokenizer(prompt, return_tensors='pt', images=image_objects)
        
        # Move inputs to the correct device
        for k, v in inputs.items():
             if v is not None and isinstance(v, torch.Tensor):
                inputs[k] = v.to(DEVICE)

        # Generate the response
        print("Generating response...")
        with torch.no_grad():
            output_ids = model.generate(
                **inputs,
                do_sample=False,
                max_new_tokens=20, # Only need a short answer (A), (B), (C), or (D)
                pad_token_id=tokenizer.eos_token_id
            )

        # Decode and clean the output
        response = tokenizer.decode(output_ids.squeeze(0), skip_special_tokens=True)
        
        # Clean the response to isolate the answer (Qwen-VL outputs the whole prompt + answer)
        answer = response.split('<|im_start|>assistant')[-1].strip().split('<|im_end|>')[0].strip()
        
        return answer
        
    except Exception as e:
        return f"An error occurred during inference: {e}"

# --- Main Execution ---
# if __name__ == "__main__":
    
#     print("--- Qwen-VL Multimodal RAG Pipeline (Offline) ---")
    
#     # 
    
#     # 1. Augmentation
#     prompt_text, images_to_process = augment_prompt_qwen_vl(RETRIEVED_TEXT, RETRIEVED_IMAGES_PATHS, QUESTION)
    
#     print("\nAugmented Prompt Ready. Running Inference...")

#     # 2. Generation
#     final_answer = run_multimodal_qa(LOCAL_MODEL_PATH, prompt_text, images_to_process)
    
#     print("\n" + "="*50)
#     print(f"QUESTION: {QUESTION}")
#     print(f"RAG ANSWER (Vietnamese): {final_answer}")
#     print("="*50)


# In[6]:


df = pd.read_csv(QUESTION_CSV)
df.head(5)


# In[44]:


processor = AutoProcessor.from_pretrained(LOCAL_MODEL_PATH, trust_remote_code=True)
model = Qwen3VLForConditionalGeneration.from_pretrained(
    LOCAL_MODEL_PATH,
    device_map=DEVICE, # Use GPU if available
    trust_remote_code=True,
    dtype = torch.bfloat16
).eval()


# In[9]:


predict = []
for i, row in tqdm(df.iterrows(), total = len(df)):
    question = row["Question"]
    ans_A = row['A']
    ans_B = row['B']
    ans_C = row['C']
    ans_D = row['D']
    choices = rf'A. {ans_A} B. {ans_B} C. {ans_C} D. {ans_D}'
    question = question + '\n' + choices
    context_text = ''
    image_prompt = ''
    
    user_message = (
        f"Đây là các thông tin được truy xuất để trả lời câu hỏi của tôi:\n"
        f"--- CONTEXT TRUY XUẤT ---\n"
        f"{context_text}\n"
        f"------------------------\n"
        f"Dựa vào thông tin trên, hãy chọn câu trả lời đúng nhất cho câu hỏi trắc nghiệm tiếng Việt sau: {question}\n"
        f"Chỉ trả lời (A), (B), (C), hoặc (D)."
    )
    
    messages = [
        {
            "role": "user",
            "content": [
#                 {
#                     "type": "image",
#                     "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
#                 },
                {"type": "text", "text": rf"{user_message}"},
            ],
        }
    ]
    
    inputs = processor.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_dict=True,
        return_tensors="pt"
    )
    inputs = inputs.to(model.device)

    # Inference: Generation of the output
    generated_ids = model.generate(**inputs, max_new_tokens=2048, do_sample=False, top_k=0, top_p=1.0)
    generated_ids_trimmed = [
        out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    with open(f'qwen3_vl_4B_instruct_predict_train/{i}.txt', 'w') as f:
        f.write('\n'.join(output_text))
    
    predict.append(output_text)


# In[13]:


post_process = [x[0].replace('(', '').replace(')', '').strip() for x in predict]
# post_process


# In[14]:


df['predict'] = post_process


# In[15]:


df.to_csv('qwen_predict_raw.csv', index = False)


# In[26]:


# correct_counter = 0
# for i, row in tqdm(df.iterrows(), total = len(df)):
#     ans = row['ans']
#     pre = row['predict']
#     if ans == pre:
#         correct_counter+= 1
#         if ',' in pre:
#             print(pre, ans)
#     else:
#         if ',' in pre:
#             print(pre, ans)
# acc = correct_counter/len(df)


# In[27]:


ans_lst = [x.replace('"', '').replace('public_test_data.zip', '') for x in df['ans']]
pre_lst = df['predict']
correct_counter= 0
for pre, ans in zip(pre_lst, ans_lst):
    if ans == pre:
        correct_counter+= 1
acc = correct_counter/len(df)
acc


# In[60]:


df['answer_correct'] = ans_lst


# In[61]:


df.to_csv('qwen_predict_raw.csv', index = False)


# # RAG

# In[29]:


with open('sentence_embedding_markdown.pkl', 'rb') as f:
    corpus_embeddings = pkl.load(f)


# In[45]:


MODEL_PATH = 'bge-m3' 
MD_FOLDER_PATH = "./var_train_full_post"  # <--- Change to your folder path


# In[46]:


WINDOW_SIZE = 3 # 2 sentences before and 2 sentences after the core sentence

# --- 1. Pure Python Sentence & Window Creation ---

def split_text_into_sentences(text: str) -> List[str]:
    """Simple, pure Python sentence splitter for Vietnamese/English punctuation."""
    # This regex splits by standard sentence-ending punctuation, followed by whitespace.
    text = text.split('\n')
    sentences = []
    for t in text:
        if t == '':
            continue
        t = re.split(r'(?<=[.?!])\s+', t.strip())[0]
        sentences.append(t)
        
    return [s.strip() for s in sentences if s.strip()]

def create_sentence_windows(folder_path: str) -> Tuple[List[str], List[Dict]]:
    """
    Loads MD files, splits into sentences, and generates contextual windows.
    Returns: (list_of_sentences_for_indexing, list_of_metadata_with_windows)
    """
    indexing_chunks = [] # The single sentence (used for embedding)
    retrieval_metadata = [] # The window (used for final output)

    print(f"Loading .md files and creating windows from: {folder_path}...")
    
    # Store all sentences sequentially to create contiguous windows across document breaks
    # (Though typically we only create windows within a single source file)
    all_sentences_with_metadata = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            filepath = os.path.join(folder_path, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()

            # Simple sentence split
            sentences = split_text_into_sentences(text)

            for sentence in sentences:
                all_sentences_with_metadata.append({
                    "sentence": sentence,
                    "source_file": filename,
                })
                
    # Now, iterate through all sentences to build the windows
    num_sentences = len(all_sentences_with_metadata)
    
    for i in range(num_sentences):
        # 1. Define window indices
        start = max(0, i - WINDOW_SIZE)
        end = min(num_sentences, i + WINDOW_SIZE + 1)
        
        # 2. Extract the context window (sentences)
        context_sentences = [all_sentences_with_metadata[j]['sentence'] 
                             for j in range(start, end) 
                             if all_sentences_with_metadata[j]['source_file'] == all_sentences_with_metadata[i]['source_file']
                            ]
        
        # 3. Create the full window string
        window = " ".join(context_sentences)
        
        # 4. Prepare indexing data and metadata
        indexing_chunks.append(all_sentences_with_metadata[i]['sentence'])
        retrieval_metadata.append({
            "source_file": all_sentences_with_metadata[i]['source_file'],
            "base_sentence": all_sentences_with_metadata[i]['sentence'],
            "context_window": window
        })
        
    return indexing_chunks, retrieval_metadata


# In[47]:


chunks, metadata = create_sentence_windows(MD_FOLDER_PATH)


# In[62]:


from FlagEmbedding import BGEM3FlagModel
print(f"Loading BGE-M3 model from: {MODEL_PATH}")
# torch.cuda.is_available() checks for GPU, but the model will run on CPU if no GPU is found
emb_model = BGEM3FlagModel(MODEL_PATH, use_fp16=torch.cuda.is_available())
# emb_model.cuda()


# In[63]:


predict = []
top_k = 3
question_embedding_arr = []
for i, row in tqdm(df.iterrows(), total = len(df)):
    question = row["Question"]
    # Retreival
    query_embeddings = emb_model.encode(
        [question], 
        batch_size=1, 
        return_dense=True, 
        return_sparse=True, 
        return_colbert_vecs=True
    )
    question_embedding_arr.append(query_embeddings)
#     similarity = query_embeddings['dense_vecs'] @ corpus_embeddings['dense_vecs'].T
#     best_doc_idx = similarity[0].argsort()[::-1]
    
#     context_text = []
#     for idx in range(len(best_doc_idx)):
#         if idx == top_k:
#             break
#         context_text.append(metadata[best_doc_idx[idx]]['context_window'])
#     context_text = '\n'.join(context_text)
#     content_arr.append(context_text)


# In[82]:


corpus_embeddings['dense_vecs'].shape


# In[85]:


corpus_embeddings['colbert_vecs'][0].shape


# In[ ]:


predict = []
top_k = 1
for i, row in tqdm(df.iterrows(), total = len(df)):
    question = row["Question"]
    # Retreival
    query_embeddings = question_embedding_arr[i]
    
    similarity = query_embeddings['dense_vecs'] @ corpus_embeddings['dense_vecs'].T
    best_doc_idx = similarity[0].argsort()[::-1]
    
    context_text = []
    for idx in range(len(best_doc_idx)):
        if idx == top_k:
            break
        context_text.append(metadata[best_doc_idx[idx]]['context_window'])
    context_text = '\n'.join(context_text)
    
    ans_A = row['A']
    ans_B = row['B']
    ans_C = row['C']
    ans_D = row['D']
    choices = rf'A. {ans_A} B. {ans_B} C. {ans_C} D. {ans_D}'
    question = question + '\n' + choices
    
    image_prompt = ''
    
    user_message = (
        f"Đây là các thông tin được truy xuất để trả lời câu hỏi của tôi:\n"
        f"--- CONTEXT TRUY XUẤT ---\n"
        f"{context_text}\n"
        f"------------------------\n"
        f"Dựa vào thông tin trên, hãy chọn câu trả lời đúng nhất cho câu hỏi trắc nghiệm tiếng Việt sau: {question}\n"
        f"Chỉ trả lời (A), (B), (C), hoặc (D)."
    )
    
    messages = [
        {
            "role": "user",
            "content": [
#                 {
#                     "type": "image",
#                     "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
#                 },
                {"type": "text", "text": rf"{user_message}"},
            ],
        }
    ]
    
    inputs = processor.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_dict=True,
        return_tensors="pt"
    )
    inputs = inputs.to(model.device)

    # Inference: Generation of the output
    generated_ids = model.generate(**inputs, max_new_tokens=2048, do_sample=False, top_k=0, top_p=1.0)
    generated_ids_trimmed = [
        out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    with open(f'qwen3_vl_4B_instruct_predict_train_rag/{i}.txt', 'w') as f:
        f.write('\n'.join(output_text))
    
    predict.append(output_text)


# In[66]:


output_text


# In[73]:


post_process = [x[0].replace('(', '').replace(')', '').strip() for x in predict]
df['predict_rag_top1'] = post_process


# In[74]:


df.to_csv('qwen_predict_rag.csv', index = False)


# In[75]:


ans_lst = [x.replace('"', '').replace('public_test_data.zip', '') for x in df['ans']]
pre_lst = df['predict_rag_top1']
correct_counter= 0
for pre, ans in zip(pre_lst, ans_lst):
    if ans == pre:
        correct_counter+= 1
acc = correct_counter/len(df)
acc


# In[ ]:




