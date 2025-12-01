import os
import pdfplumber
import pandas as pd
import numpy as np
import re
pd.set_option('future.no_silent_downcasting', True)
# --- 1. FORMATTING & HEADING LOGIC ---

def is_bold(font_name):
    """Checks if the font name contains keywords suggesting 'Bold'."""
    return 'bold' in font_name.lower() or 'black' in font_name.lower()

def is_italic(font_name):
    """Checks if the font name contains keywords suggesting 'Italic'."""
    return 'italic' in font_name.lower() or 'oblique' in font_name.lower()

def get_word_format_type(font_name):
    """Determines the format type: 'bold', 'italic', or 'none'."""
    if is_bold(font_name):
        return 'bold'
    if is_italic(font_name):
        return 'italic'
    return 'none'

def dataframe_to_custom_html(df: pd.DataFrame) -> str:
    """
    Converts a Pandas DataFrame into a highly customized HTML table structure
    where every cell is wrapped in <blockquote><p> tags and headers are bolded.
    """
    html_parts = []
    
    # Start Table
    html_parts.append("<table>")

    # 1. Generate Colgroup (one <col/> for each column)
    html_parts.append("<colgroup>")
    for _ in df.columns:
        html_parts.append("<col/>")
    html_parts.append("</colgroup>")

    # 2. Generate Table Header (<thead>)
    html_parts.append("<thead>")
    html_parts.append("<tr>")
    
    for col in df.columns:
        # Header cell requires <blockquote><p><strong>...</strong></p></blockquote>
        header_content = f"<blockquote><p><strong>{col}</strong></p></blockquote>"
        html_parts.append(f"<th>{header_content}</th>")
        
    html_parts.append("</tr>")
    html_parts.append("</thead>")

    # 3. Generate Table Body (<tbody>)
    html_parts.append("<tbody>")
    
    # Iterate through rows
    for _, row in df.iterrows():
        html_parts.append("<tr>")
        
        # Iterate through cells in the row
        for cell_value in row:
            # Data cell requires <blockquote><p>...</p></blockquote>
            # Convert cell value to string to handle mixed types
            cell_str = str(cell_value)
            data_content = f"<blockquote><p>{cell_str}</p></blockquote>"
            html_parts.append(f"<td>{data_content}</td>")
            
        html_parts.append("</tr>")
        
    html_parts.append("</tbody>")
    
    # End Table
    html_parts.append("</table>")
    
    return "\n".join(html_parts)

def process_block(block):
    """
    Wraps a text block with appropriate Markdown syntax.
    
    If the block is bold and starts with a numbered list (e.g., "1. "), 
    it is treated as a special [DIGITAL] heading, and the numbering is removed.
    """
    # Join words into a single string
    text = " ".join(block['words'])
    
    # Regex pattern: start of string (^), one or more digits (\d+), dot (\.), space (\s)
    ordered_list_pattern = re.compile(r"^\d+\.\s")
    ordered_sublist_pattern = re.compile(r"^\d+\.\d+")
    ordered_subsublist_pattern = re.compile(r"^\d+\.\d+\.\d+")


    
    # 1. Check for [DIGITAL] Heading (Highest Priority)
    if block['type'] == 'bold' and ordered_subsublist_pattern.match(text):
        return "### " + text
    if block['type'] == 'bold' and ordered_sublist_pattern.match(text):
        # Remove the numbering part (e.g., "1.1. ")
        # cleaned_text = re.sub(ordered_sublist_pattern, "## ", text, count=1)
        # Apply the [DIGITAL] prefix
        return "## "+ text
    elif block['type'] == 'bold' and ordered_list_pattern.match(text):
        # Remove the numbering part (e.g., "1. ")
        # cleaned_text = re.sub(ordered_list_pattern, "# ", text, count=1)
        # Apply the [DIGITAL] prefix
        return "# " + text
        
    # 2. Regular Bold Formatting
    elif block['type'] == 'bold':
        return f"**{text}** "
        
    # 3. Italic Formatting
    elif block['type'] == 'italic':
        return f"*{text}* "
        
    # 4. No Formatting
    else:
        return text

# --- 2. TABLE PROCESSING LOGIC ---

def pdfplumber_table_to_markdown(table):
    """Converts a pdfplumber Table object to a Markdown string."""
    
    data = table.extract()
    if not data or not data[0]:
        return ""
    
    # Use Pandas for clean conversion to Markdown table syntax
    df = pd.DataFrame(data)
    
    
    # Fill None/NaN with empty strings for clean Markdown rendering
    df = df.replace(r'^\s*$', np.nan, regex=True).fillna('') 

    if len(df) > 1:
        header = df.iloc[0].astype(str).fillna('')
        df_no_header = df[1:].copy().reset_index(drop=True)
        df_no_header.columns = header
    else:
        # Nếu chỉ có một hàng (chỉ header), tạo DataFrame rỗng với header đó
        header = df.iloc[0].astype(str).fillna('') if len(df) == 1 else []
        df_no_header = pd.DataFrame(columns=header)
    html_table = dataframe_to_custom_html(df_no_header)
    # markdown_output = df_no_header.to_markdown(index=False)
    # Add extra lines for separation
    return "\n" + html_table + "\n\n"

# --- 3. CORE STITCHING LOGIC ---

def get_block_type_and_filter(line, table_bboxes):
    """
    Checks if a text line overlaps with any table bbox. 
    Returns the line object if it's external text, otherwise returns None (filtered out).
    """
    # Get Y coordinates of the text line
    line_y_top = line['top']
    line_y_bottom = line['bottom']
    
    for t_x0, t_top, t_x1, t_bottom in table_bboxes:
        # Check for overlap in the Y-axis
        # If the line is fully contained within the table's Y range, filter it out.
        if t_top <= line_y_top < t_bottom and t_top < line_y_bottom <= t_bottom:
             return None # It's part of a table, discard the text line
    
    # If it passed the filter, return the line object
    return line

def merge_formatted_blocks(page_id, formatted_words):
    """
    Merges consecutive words with the same formatting into a list of structured 
    content blocks, suitable for positional stitching.
    """
    if not formatted_words:
        return []
    
    # This list will hold the final dictionary blocks
    result_blocks = []
    current_block = None
    block_start_top = None # To track the 'top' coordinate of the starting word
    
    # Ensure words are sorted by position before merging (Top then X-axis)
    # The calling function (pdf_to_markdown_pipeline) usually does this, 
    # but it's good practice to ensure here as well.

    new_words = []
    for word in formatted_words:
        if word['text'] == "\n":
            continue
        new_words.append(word)
    formatted_words = new_words
    
    formatted_words.sort(key=lambda w: (w['top'], w['x0']))



    list_words = [w['text'] for w in formatted_words]
    # if page_id == 4:
    #     import ipdb; ipdb.set_trace()
    for i, word in enumerate(formatted_words):
        # Check if this word is on the same line as the previous word (Y coordinate check)
        is_same_line = False
        if i > 0:
            if abs(word['top'] - formatted_words[i-1]['top']) < 7:
                is_same_line = True
            elif formatted_words[i-1]['x1'] > 507 and not word['text'][0].isupper():
                # Special case: if previous word is at the far right and current word starts with lowercase,
                # consider it as same line (likely a line continuation)
                is_same_line = True
                # if page_id == 2:
                    # print("Special line continuation detected:", formatted_words[i-1]['text'], "->", word['text'])
                    # print(formatted_words[i-1], word, formatted_words[i+1])
        
                
        if current_block is None:
            # Start the very first block
            current_block = {'type': word['type'], 'words': [word['text']]}
            block_start_top = word['top'] # Capture starting position
            continue
        
        # If line break detected OR format changes:
        if not is_same_line or word['type'] != current_block['type']:
            
            # --- END OF CURRENT BLOCK ---
            # 1. Process the finished block and append to results list
            # We use the captured 'top' coordinate of the *starting* word
            result_blocks.append({
                'type': 'text',
                'top': block_start_top,
                'content': process_block(current_block)
            })
            
            # --- START OF NEW BLOCK ---
            # 2. Initialize the new block with the current word
            current_block = {'type': word['type'], 'words': [word['text']]}
            block_start_top = word['top'] # Capture starting position of the new block
        
        else:
            current_block['words'].append(word['text'])
    
    # Process the very last block after the loop ends
    if current_block:
        result_blocks.append({
            'type': 'text',
            'top': block_start_top,
            'content': process_block(current_block)
        })
        
    return result_blocks


def treat_page_with_llm(page):
    page_image = page.to_image(resolution=300)
    # Load and do a quick pass over "sample/result.mmd" for further processing
    result_mmd_path = "sample/result.mmd"

    prompt = "<image>\n<|grounding|>Convert the document to markdown. "
    image_file ="temp.png"
    page_image.save(image_file)
    output_path = "temp_result"
    os.makedirs(output_path, exist_ok=True)


    res = model.infer(tokenizer, prompt=prompt, image_file=image_file, output_path = output_path, 
                      base_size = 1024, image_size = 640, crop_mode=True, save_results = True, test_compress = True)



    # Read file
    with open(os.path.join(output_path, "result.mmd"), "r", encoding="utf-8") as f:
        result_mmd = f.read()

    # Basic derived variables for downstream cells
    result_mmd_lines = result_mmd.splitlines()
    result_mmd_blocks = result_mmd.split("\n\n")

    # Find referenced image placeholders like <image_1>
    image_refs = re.findall(r"<image_(\d+)>", result_mmd)
    image_refs = sorted(set(image_refs), key=lambda s: int(s))

    table_refs = re.findall(r"<table>", result_mmd)

    fintune_blocks = []
    for block in result_mmd_blocks:
        if "<table>" in block and "VIETTEL AI RACE" in block:
            continue
        if "<table>" in block:
            # Replace with processed table markdown
            block = block.replace("<td>", "<td><em>")
            block = block.replace("<tr>", "<tr>\n")
            block = block.replace("<table>", "<table>\n")



            block = block.replace("</td>", "</em></td>\n")
        fintune_blocks.append(block)
    mkdown = "\n\n".join(fintune_blocks)
    return mkdown



# --- 4. MAIN PIPELINE ---
import io
from PIL import Image
def pdf_to_markdown_pipeline(pdf_path, output_path):
    """
    The main pipeline to convert PDF content to Markdown, handling tables,
    formatting, and positional stitching.
    """
    folder_image = output_path.replace('.md','') + "/images"
    os.makedirs(folder_image, exist_ok=True)

    markdown_content = []
    
    with pdfplumber.open(pdf_path) as pdf:
        print(f"\n******Processing file: {pdf_path} with {len(pdf.pages)} pages...\n")
        id_image = 1
        
        for i, page in enumerate(pdf.pages):
            images_block = []

            # if i != 15:
            #     continue

            # extract image
            imgs = page.images
            for id_img, img in enumerate(imgs):
                if img['top'] < 70:
                    continue
                content = f"|<image_{id_image}>|"
                
                raw = img["stream"].get_data()
                # open with Pillow to decode
                try:
                    image = Image.open(io.BytesIO(raw))
                except Exception as e:
                    print(f"Error opening image {id_image} on page {i+1}: {e}")
                    continue
                images_block.append({
                    'type': 'image',
                    'top': img['top'],
                    'content': content
                })

                # choose filename
                filename = f"{folder_image}/image_{id_image}.png"
                

                image.save(filename)

                id_image += 1

            area_table = 0
            area_page = page.width * page.height
            
            # --- Step 1: Extract Tables and Text Lines ---
            tables = page.find_tables()
            table_bboxes = [t.bbox for t in tables]
            
            text_lines = page.extract_text_lines(T_y_tolerance=3)
            
            # --- Step 2: Filter Text and Prepare Content Blocks ---
            
            # List to hold all content objects (Text or Table) with their position
            content_blocks = []
            
            # a. Prepare Table Blocks
            for table in tables:
                content_blocks.append({
                    'type': 'table',
                    'top': table.bbox[1], 
                    'content': pdfplumber_table_to_markdown(table)
                })
                bbox = table.bbox
                width = bbox[2] - bbox[0]
                height = bbox[3] - bbox[1]
                area_table += (width*height)
            # if area_table/area_page > 0.38:
            #     print("page", i, "area table", area_table/area_page, "processing with llm")

            #     page_content = treat_page_with_llm(page)
            #     markdown_content.append(page_content)
            #     continue
            # b. Filter and Group Text Lines
            # The text processing is complex:
            # 1. We must process 'words' to get formatting information.
            # 2. We must use 'text_lines' to get accurate positioning for filtering.
            
            # Extract all formatted words on the page
            all_formatted_words = []
            words = page.extract_words()
            chars = page.chars
            
            for word in words:
                # Get font name (assume one font per word)
                word_chars = [c for c in chars if c['x0'] >= word['x0'] and c['x1'] <= word['x1'] and c['top'] >= word['top'] and c['bottom'] <= word['bottom']]
                
                font_name = word_chars[0]['fontname'] if word_chars else 'none'
                
                # Store as a list of word objects
                all_formatted_words.append({
                    'text': word['text'],
                    'type': get_word_format_type(font_name),
                    'top': word['top'], 
                    'bottom': word['bottom'],
                    'x0': word['x0'],
                    'x1': word['x1']
                })

            # c. Group and Filter Formatted Words into Text Blocks
            text_blocks_to_merge = []
            
            # Group words into lines based on Y coordinate
            current_line_words = []
            last_bottom = 0
            
            # Sort words primarily by 'top' (Y-axis) and secondarily by 'x0' (X-axis)
            all_formatted_words.sort(key=lambda w: (w['top'], w['x0']))
            
            for word in all_formatted_words:
                # Check for line break (if current word's top is significantly different from the last word's bottom)
                if current_line_words and (word['top'] > last_bottom + 7): 
                    # Process the previous line
                    if not current_line_words: continue

                    # Check if this line overlaps with any table (using the whole line's bbox)
                    line_top = min(w['top'] for w in current_line_words)
                    line_bottom = max(w['bottom'] for w in current_line_words)
                    line_x0 = min(w['x0'] for w in current_line_words)
                    line_x1 = max(w['x1'] for w in current_line_words)
                    
                    line_bbox = (line_x0, line_top, line_x1, line_bottom)
                    
                    # Apply table filtering logic
                    is_external_text = get_block_type_and_filter({'top': line_top, 'bottom': line_bottom}, table_bboxes)

                    if is_external_text is not None:
                        text_blocks_to_merge.extend(current_line_words)
                        text_blocks_to_merge.append({'text': '\n', 'type': 'line_break', 'top': line_bottom, 'bottom': line_bottom, 'x0': 0, 'x1': 0})

                    current_line_words = []
                
                current_line_words.append(word)
                last_bottom = word['bottom']

            # Process the last line
            if current_line_words:
                line_top = min(w['top'] for w in current_line_words)
                line_bottom = max(w['bottom'] for w in current_line_words)
                
                is_external_text = get_block_type_and_filter({'top': line_top, 'bottom': line_bottom}, table_bboxes)

                if is_external_text is not None:
                    text_blocks_to_merge.extend(current_line_words)
            
            # 4. Merge Formatted Blocks and Prepare for Stitching
            # The merge_formatted_blocks function implicitly handles line breaks and formatting
            text_blocks = merge_formatted_blocks(i, text_blocks_to_merge)
            content_blocks.extend(text_blocks)
            content_blocks.extend(images_block)

            # --- Step 5: Stitch Content Blocks by Position ---
            
            # Sort all content (Text and Table) based on 'top' coordinate (Y-axis)
            content_blocks.sort(key=lambda x: x['top'])
            if content_blocks[0]['type'] == 'table' and "VIETTEL AI RACE" in content_blocks[0]['content']:
                content_blocks = content_blocks[1:]
            # if i==4:
            #     import ipdb; ipdb.set_trace()   
            # Append to final output
            page_markdown = [block['content'] for block in content_blocks]
            
            # markdown_content.append(f"## Page {i + 1}\n")
            markdown_content.extend(page_markdown)
            # if i == 2:
            #     break
    markdown_content = "\n\n".join(markdown_content)
    markdown_content = markdown_content.replace("\n- ", "\n\- ")
    markdown_content = markdown_content.replace("\n+ ", "\n\+ ")

    filename = pdf_path.split('/')[-1].split('.pdf')[0]
    markdown_content = "# " + filename+"\n\n" + markdown_content
    markdown_content = markdown_content.replace("foo", "")

    # markdown_content = re.sub(r'\s\n.', ' ', markdown_content)
    # markdown_content = markdown_content.replace(' \n', ' ')
    # Write result to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
        
    print(f"\n✅ Conversion successful! Output saved at: {output_path}")



# --- EXECUTION ---
if __name__ == "__main__":
    # input_pdf_file = "./sample/gt/Public_257.pdf" 
    # output_md_file = input_pdf_file.replace('.pdf', '.md').replace("gt","pred")
    # pdf_to_markdown_pipeline(input_pdf_file, output_md_file)

    folder_pdf = "./data/var_test/pdf"
    folder_md = "./markdown_pred/"
    
    os.makedirs(folder_md, exist_ok=True)
    # from transformers import AutoModel, AutoTokenizer
    # import torch
    # import os
    # os.environ["CUDA_VISIBLE_DEVICES"] = '0'
    # model_name = '../Deepseek_OCR'

    # tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    # model = AutoModel.from_pretrained(model_name, _attn_implementation='flash_attention_2', trust_remote_code=True, use_safetensors=True)
    # model = model.eval().cuda().to(torch.bfloat16)
    # Ensure 'input.pdf' exists in the same directory
    list_pdf = os.listdir(folder_pdf)
    list_pdf.sort()
    for pdf_file in list_pdf:
        input_pdf_file = os.path.join(folder_pdf, pdf_file)
        output_md_file = os.path.join(folder_md, pdf_file.replace('.pdf', '.md'))
        pdf_to_markdown_pipeline(input_pdf_file, output_md_file)