#!/usr/bin/env python
# coding: utf-8

# In[108]:


import os
import torch
import re
from FlagEmbedding import BGEM3FlagModel
from typing import List, Dict, Tuple
import pandas as pd
import pickle as pkl


# In[102]:


# --- Configuration ---
# IMPORTANT: If offline, replace 'BAAI/bge-m3' with the path to your downloaded model directory.
MODEL_PATH = 'bge-m3' 
MD_FOLDER_PATH = "./var_train_full_post"  # <--- Change to your folder path
QUERY = "Quy trình báo cáo lỗi hệ thống như thế nào?" # <--- Your Vietnamese Question


# In[103]:


WINDOW_SIZE = 10 # 2 sentences before and 2 sentences after the core sentence

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


# In[104]:


# --- 2. Main Offline Retrieval and Ranking ---
# def main():
#     # A. Load Data
#     chunks, metadata = load_and_chunk_md_files(MD_FOLDER_PATH)
#     if not chunks:
#         print("No markdown files found or content is empty after splitting.")
#         return

#     # B. Load BGE-M3 Model (Must be locally available!)
#     print(f"Loading BGE-M3 model from: {MODEL_PATH}")
#     # torch.cuda.is_available() checks for GPU, but the model will run on CPU if no GPU is found
#     model = BGEM3FlagModel(MODEL_PATH, use_fp16=torch.cuda.is_available())

#     # C. Embed Corpus
#     print(f"Encoding {len(chunks)} chunks... (This may be slow on CPU)")
#     corpus_embeddings = model.encode(
#         chunks, 
#         batch_size=12, 
#         max_length=8192,
#         return_dense=True, 
#         return_sparse=True, 
#         return_colbert_vecs=True
#     )
    
#     # D. Embed Query
#     query_embeddings = model.encode(
#         [QUERY], 
#         batch_size=1, 
#         return_dense=True, 
#         return_sparse=True, 
#         return_colbert_vecs=True
#     )

#     # E. Hybrid Ranking (The BGE-M3 Advantage)
#     # Weights for the combined score: [Dense, Sparse, ColBERT]
#     # The default 1:1:1 weighting often provides the best balance.
#     print("Ranking documents using hybrid scoring...")
#     scores = model.compute_score(
#         query_embeddings, 
#         corpus_embeddings, 
#         weights_for_different_modes=[1.0, 1.0, 1.0] 
#     )

#     # Get the final combined score list
#     combined_scores = scores['colbert+sparse+dense']

#     # F. Find Top Result
#     # argmax gives the index of the highest score
#     best_doc_idx = combined_scores[0].argmax() 
#     best_score = combined_scores[0][best_doc_idx]
    
#     best_chunk = metadata[best_doc_idx]

#     # --- Print Results ---
#     print("\n" + "="*70)
#     print(f"BGE-M3 OFFLINE RETRIEVAL RESULT FOR: '{QUERY}'")
#     print("="*70)
#     print(f"🎯 TOP MATCH FOUND IN FILE: **{best_chunk['source_file']}**")
#     print(f"📈 COMBINED HYBRID SCORE: {best_score:.4f}")
#     print("-" * 70)
#     print("CONTEXT (Headers):")
#     # Display headers cleanly
#     header_info = " / ".join(f"{k}: {v}" for k, v in best_chunk['headers'].items())
#     print(f"  {header_info}")
#     print("-" * 70)
#     print("RELEVANT CHUNK CONTENT (Snippet):")
#     # Print the full content of the chunk found
#     print(best_chunk['content'][:500] + "...") 
#     print("="*70)


# In[105]:


chunks, metadata = create_sentence_windows(MD_FOLDER_PATH)


# In[106]:


print(f"Loading BGE-M3 model from: {MODEL_PATH}")
# torch.cuda.is_available() checks for GPU, but the model will run on CPU if no GPU is found
model = BGEM3FlagModel(MODEL_PATH, use_fp16=torch.cuda.is_available())


# In[107]:


corpus_embeddings = model.encode(
        chunks, 
        batch_size=12, 
        max_length=1024,
        return_dense=True, 
        return_sparse=True, 
        return_colbert_vecs=True
    )


# In[110]:


with open('sentence_embedding_markdown.pkl', 'wb') as f:
    pkl.dump(corpus_embeddings, f)


# In[92]:


question_csv = pd.read_csv('/workspace/VAR2025/OCR/data/public_test_data/question.csv')
top_k = 3
for i, row in question_csv.iterrows():
    question = row["Question"]
    
#     sentence_pairs = [[i,j] for i in question for j in chunks[:10]]
#     scores = model.compute_score(
#         sentence_pairs, 
#         max_passage_length=128, 
#         weights_for_different_modes=[1.0, 1.0, 1.0] 
#     )
    query_embeddings = model.encode(
        [question], 
        batch_size=1, 
        return_dense=True, 
        return_sparse=True, 
        return_colbert_vecs=True
    )
    
    similarity = query_embeddings['dense_vecs'] @ corpus_embeddings['dense_vecs'].T
    best_doc_idx = similarity[0].argsort()[::-1]

#     # E. Hybrid Ranking (The BGE-M3 Advantage)
#     # Weights for the combined score: [Dense, Sparse, ColBERT]
#     # The default 1:1:1 weighting often provides the best balance.
#     print("Ranking documents using hybrid scoring...")
#     scores = model.compute_score(
#         query_embeddings, 
#         corpus_embeddings, 
#         weights_for_different_modes=[1.0, 1.0, 1.0] 
#     )

#     # Get the final combined score list
#     combined_scores = scores['colbert+sparse+dense']

#     # F. Find Top Result
#     # argmax gives the index of the highest score
#     best_doc_idx = combined_scores[0].argsort() 
#     best_score = combined_scores[0][best_doc_idx]
    break


# In[100]:


row


# In[96]:


print(question)
print('-'*123)
for idx in range(len(best_doc_idx)):
    if idx == top_k:
        break
    print(metadata[best_doc_idx[idx]])


# In[95]:


print(idx)


# In[87]:


similarity[0].shape


# In[99]:


similarity[0][best_doc_idx][:10]


# In[ ]:




