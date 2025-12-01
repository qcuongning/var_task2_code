import os
import io
import re
from typing import List, Dict, Any, Optional, Tuple

import pdfplumber
import pandas as pd
import numpy as np
from PIL import Image

pd.set_option('future.no_silent_downcasting', True)

# Compile regexes once at module load to avoid recompilation
_RE_ORDERED_LIST = re.compile(r"^\d+\.\s")
_RE_ORDERED_SUBLIST = re.compile(r"^\d+\.\d+")
_RE_ORDERED_SUBSUB = re.compile(r"^\d+\.\d+\.\d+")
# --- 1. FORMATTING & HEADING LOGIC ---

# regen-prompt: "Implement is_bold(font_name: str) -> bool: return True when font name suggests bold/black (case-insensitive)."
def is_bold(font_name: str) -> bool:
    """Return True if the font name suggests bold weight (case-insensitive)."""
    if not font_name:
        return False
    fname = font_name.lower()
    return "bold" in fname or "black" in fname

# regen-prompt: "Implement is_italic(font_name: str) -> bool: detect italic/oblique in font name (case-insensitive)."
def is_italic(font_name: str) -> bool:
    """Return True if the font name suggests italic or oblique style."""
    if not font_name:
        return False
    fname = font_name.lower()
    return "italic" in fname or "oblique" in fname

# regen-prompt: "Implement get_word_format_type(font_name: str) -> str: return 'bold'|'italic'|'none' based on font_name."
def get_word_format_type(font_name: str) -> str:
    """Return one of 'bold', 'italic', or 'none' based on the provided font name."""
    if is_bold(font_name):
        return "bold"
    if is_italic(font_name):
        return "italic"
    return "none"

# regen-prompt: "Implement dataframe_to_custom_html(df: pd.DataFrame) -> str: produce table HTML where headers are bold and every cell wrapped in <blockquote><p>..</p></blockquote>."
def dataframe_to_custom_html(df: pd.DataFrame) -> str:
    """Convert a DataFrame to a custom HTML table where headers are bold and
    each cell is wrapped in <blockquote><p>..</p></blockquote>.

    This function keeps a minimal, predictable structure and converts all
    values to strings to avoid rendering issues.
    """
    html_parts: List[str] = ["<table>"]

    # Colgroup
    html_parts.append("<colgroup>")
    html_parts.extend(["<col/>" for _ in df.columns])
    html_parts.append("</colgroup>")

    # Thead
    html_parts.append("<thead>")
    html_parts.append("<tr>")
    for col in df.columns:
        header_content = f"<blockquote><p><strong>{col}</strong></p></blockquote>"
        html_parts.append(f"<th>{header_content}</th>")
    html_parts.append("</tr>")
    html_parts.append("</thead>")

    # Tbody
    html_parts.append("<tbody>")
    for _, row in df.iterrows():
        html_parts.append("<tr>")
        for cell_value in row:
            cell_str = "" if pd.isna(cell_value) else str(cell_value)
            data_content = f"<blockquote><p>{cell_str}</p></blockquote>"
            html_parts.append(f"<td>{data_content}</td>")
        html_parts.append("</tr>")
    html_parts.append("</tbody>")

    html_parts.append("</table>")
    return "\n".join(html_parts)

# regen-prompt: "Implement process_block(block: dict) -> str: join block['words'] and wrap with markdown based on block['type'] and leading ordered list patterns."
def process_block(block: Dict[str, Any]) -> str:
    """Convert a merged block (words+type) into a markdown string.

    Headings are created when bold text starts with ordered-list-like prefixes.
    Bold -> **text**, Italic -> *text*; numbered bold lines become headings.
    """
    text = " ".join(block.get("words", []))

    # Ordered-list based headings have precedence
    if block.get("type") == "bold":
        if _RE_ORDERED_SUBSUB.match(text):
            return "### " + text
        if _RE_ORDERED_SUBLIST.match(text):
            return "## " + text
        if _RE_ORDERED_LIST.match(text):
            return "# " + text
        return f"**{text}**"

    if block.get("type") == "italic":
        return f"_{text}_"

    return text

# --- 2. TABLE PROCESSING LOGIC ---

# regen-prompt: "Implement pdfplumber_table_to_markdown(table) -> str: extract table to DataFrame, treat first row as header if present, return custom HTML table string."
def pdfplumber_table_to_markdown(table: Any) -> str:
    """Convert a pdfplumber Table into custom HTML (wrapped as markdown block).

    The first row is interpreted as header if there is more than one row. Empty
    cells are normalized to empty strings.
    """
    data = table.extract()
    if not data or not data[0]:
        return ""

    df = pd.DataFrame(data)
    # Normalize blank-like strings to NaN, then fill with empty string
    df = df.replace(r"^\s*$", np.nan, regex=True).fillna("")

    if len(df) > 1:
        header = df.iloc[0].astype(str).fillna("")
        df_no_header = df[1:].copy().reset_index(drop=True)
        df_no_header.columns = header
    else:
        header = df.iloc[0].astype(str).fillna("") if len(df) == 1 else []
        df_no_header = pd.DataFrame(columns=header)

    html_table = dataframe_to_custom_html(df_no_header)
    return "\n" + html_table + "\n\n"

# --- 3. CORE STITCHING LOGIC ---

# regen-prompt: "Implement get_block_type_and_filter(line: dict, table_bboxes: list) -> Optional[dict]: if line fully inside any table bbox return None else the line."
def get_block_type_and_filter(line: Dict[str, float], table_bboxes: List[Tuple[float, float, float, float]]) -> Optional[Dict[str, float]]:
    """Return None when a text line appears fully inside any table bbox.

    Table bboxes come as (x0, top, x1, bottom). We consider a line part of a
    table only if both its top and bottom are within the table vertical range.
    """
    line_y_top = line.get("top", 0)
    line_y_bottom = line.get("bottom", 0)

    for t_x0, t_top, t_x1, t_bottom in table_bboxes:
        if t_top <= line_y_top < t_bottom and t_top < line_y_bottom <= t_bottom:
            return None
    return line

# regen-prompt: "Implement merge_formatted_blocks(page_id: int, formatted_words: List[dict]) -> List[dict]: merge adjacent words with same format into blocks keeping top coordinate; treat small top differences as same line."
def merge_formatted_blocks(page_id: int, formatted_words: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Merge consecutive words that share formatting into larger content blocks.

    This function preserves the 'top' of the first word of a block and returns
    a list of {'type': 'text', 'top': float, 'content': str} items produced by
    `process_block`.
    """
    if not formatted_words:
        return []

    # Remove explicit newline tokens and sort by vertical then horizontal position
    words = [w for w in formatted_words if w.get("text") != "\n"]
    words.sort(key=lambda w: (w.get("top", 0), w.get("x0", 0)))

    result_blocks: List[Dict[str, Any]] = []
    current_block: Optional[Dict[str, Any]] = None
    block_start_top: float = 0.0

    for i, word in enumerate(words):
        is_same_line = False
        if i > 0:
            prev = words[i - 1]
            # small vertical displacement -> same line
            if abs(word.get("top", 0) - prev.get("top", 0)) < 7:
                is_same_line = True
            # heuristic line-continuation: previous word near right edge and this starts lowercase
            elif prev.get("x1", 0) > 507 and word.get("text", "")[0:1].islower():
                is_same_line = True

        if current_block is None:
            current_block = {"type": word.get("type"), "words": [word.get("text", "")]}
            block_start_top = word.get("top", 0)
            continue

        # boundary when line breaks or style changes
        if not is_same_line or word.get("type") != current_block.get("type"):
            result_blocks.append({
                "type": "text",
                "top": block_start_top,
                "content": process_block(current_block),
            })
            current_block = {"type": word.get("type"), "words": [word.get("text", "")]}
            block_start_top = word.get("top", 0)
        else:
            current_block.setdefault("words", []).append(word.get("text", ""))

    if current_block:
        result_blocks.append({
            "type": "text",
            "top": block_start_top,
            "content": process_block(current_block),
        })

    return result_blocks


# regen-prompt: "Implement treat_page_with_llm(page) -> str: save page image, call model.infer with prompt and return cleaned result.mmd content as markdown string."
def treat_page_with_llm(page: Any) -> str:
    """Fallback when a page is mostly tables: render page image and ask LLM to convert.

    This function relies on `model` and `tokenizer` available in the module
    scope (the original script sets them up in __main__). It saves a temporary
    image and reads back `result.mmd` produced by the inference routine.
    """
    page_image = page.to_image(resolution=300)
    image_file = "temp.png"
    page_image.save(image_file)
    output_path = "temp_result"
    os.makedirs(output_path, exist_ok=True)

    prompt = "<image>\n<|grounding|>Convert the document to markdown. "

    # Call model.infer; keep call defensive in case model/tokenizer not present
    try:
        _ = model.infer(
            tokenizer,
            prompt=prompt,
            image_file=image_file,
            output_path=output_path,
            base_size=1024,
            image_size=640,
            crop_mode=True,
            save_results=True,
            test_compress=True,
        )
    except Exception:
        # If inference fails, return an empty placeholder so pipeline continues
        return ""

    mmd_path = os.path.join(output_path, "result.mmd")
    if not os.path.exists(mmd_path):
        return ""

    with open(mmd_path, "r", encoding="utf-8") as f:
        result_mmd = f.read()

    blocks = []
    for block in result_mmd.split("\n\n"):
        if "<table>" in block and "VIETTEL AI RACE" in block:
            continue
        if "<table>" in block:
            block = block.replace("<td>", "<td><em>")
            block = block.replace("<tr>", "<tr>\n")
            block = block.replace("<table>", "<table>\n")
            block = block.replace("</td>", "</em></td>\n")
        blocks.append(block)

    return "\n\n".join(blocks)



# --- 4. MAIN PIPELINE ---
def pdf_to_markdown_pipeline(pdf_path, output_path):
    """
    The main pipeline to convert PDF content to Markdown, handling tables,
    formatting, and positional stitching.
    """
    folder_image = output_path.replace('.md', '') + "/images"
    os.makedirs(folder_image, exist_ok=True)

    markdown_content: List[str] = []
    print(f"\n******Processing file: {pdf_path}\n")
    with pdfplumber.open(pdf_path) as pdf:
        id_image = 1

        for i, page in enumerate(pdf.pages):
            images_block: List[Dict[str, Any]] = []

            # extract images (skip headers/top decorations)
            for img in page.images:
                if img.get('top', 0) < 70:
                    continue
                content = f"|<image_{id_image}>|"
                raw = img.get("stream").get_data() if img.get("stream") else None
                if raw is None:
                    continue
                try:
                    image = Image.open(io.BytesIO(raw))
                except Exception as e:
                    print(f"Error opening image {id_image} on page {i+1}: {e}")
                    continue
                filename = f"{folder_image}/image_{id_image}.png"
                image.save(filename)
                images_block.append({"type": "image", "top": img.get('top', 0), "content": content})
                id_image += 1

            area_table = 0.0
            area_page = page.width * page.height

            # Step 1: Extract tables and text lines
            tables = page.find_tables()
            table_bboxes = [t.bbox for t in tables]

            # Step 2: Prepare content blocks list (tables first)
            content_blocks: List[Dict[str, Any]] = []
            for table in tables:
                content_blocks.append({"type": "table", "top": table.bbox[1], "content": pdfplumber_table_to_markdown(table)})
                bbox = table.bbox
                area_table += (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])

            # If a large portion of page is table, delegate to LLM treatment
            if area_table / max(area_page, 1.0) > 0.38:
                print("page", i, "area table", area_table / max(area_page, 1.0), "processing with llm")
                page_content = treat_page_with_llm(page)
                if page_content:
                    markdown_content.append(page_content)
                continue

            # Extract chars/words and annotate formatting
            all_formatted_words: List[Dict[str, Any]] = []
            words = page.extract_words()
            chars = page.chars

            for word in words:
                # find chars that fall within the word box
                word_chars = [c for c in chars if c.get('x0', 0) >= word.get('x0', 0) and c.get('x1', 0) <= word.get('x1', 0) and c.get('top', 0) >= word.get('top', 0) and c.get('bottom', 0) <= word.get('bottom', 0)]
                font_name = word_chars[0].get('fontname') if word_chars else ''
                all_formatted_words.append({
                    'text': word.get('text', ''),
                    'type': get_word_format_type(font_name),
                    'top': word.get('top', 0),
                    'bottom': word.get('bottom', 0),
                    'x0': word.get('x0', 0),
                    'x1': word.get('x1', 0),
                })

            # Group words into lines and filter those inside tables
            text_blocks_to_merge: List[Dict[str, Any]] = []
            current_line_words: List[Dict[str, Any]] = []
            last_bottom = 0

            all_formatted_words.sort(key=lambda w: (w['top'], w['x0']))

            for word in all_formatted_words:
                if current_line_words and (word['top'] > last_bottom + 7):
                    # process the previous line
                    line_top = min(w['top'] for w in current_line_words)
                    line_bottom = max(w['bottom'] for w in current_line_words)
                    is_external = get_block_type_and_filter({'top': line_top, 'bottom': line_bottom}, table_bboxes)
                    if is_external is not None:
                        text_blocks_to_merge.extend(current_line_words)
                        text_blocks_to_merge.append({'text': '\n', 'type': 'line_break', 'top': line_bottom, 'bottom': line_bottom, 'x0': 0, 'x1': 0})
                    current_line_words = []

                current_line_words.append(word)
                last_bottom = word.get('bottom', last_bottom)

            if current_line_words:
                line_top = min(w['top'] for w in current_line_words)
                line_bottom = max(w['bottom'] for w in current_line_words)
                is_external = get_block_type_and_filter({'top': line_top, 'bottom': line_bottom}, table_bboxes)
                if is_external is not None:
                    text_blocks_to_merge.extend(current_line_words)

            # Merge blocks and collect content
            text_blocks = merge_formatted_blocks(i, text_blocks_to_merge)
            content_blocks.extend(text_blocks)
            content_blocks.extend(images_block)

            # Stitch by vertical position
            if content_blocks:
                content_blocks.sort(key=lambda x: x['top'])
                if content_blocks and content_blocks[0].get('type') == 'table' and "VIETTEL AI RACE" in content_blocks[0].get('content', ''):
                    content_blocks = content_blocks[1:]

            page_markdown = [block.get('content', '') for block in content_blocks]
            markdown_content.extend(page_markdown)

    markdown_text = "\n\n".join(markdown_content)
    markdown_text = markdown_text.replace("\n- ", "\n\\- ").replace("\n+ ", "\n\\+ ")

    filename = os.path.basename(pdf_path).split('.pdf')[0]
    markdown_text = "# " + filename + "\n\n" + markdown_text
    markdown_text = markdown_text.replace("foo", "")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_text)

    print(f"\n✅ Conversion successful! Output saved at: {output_path}")



# --- EXECUTION ---
if __name__ == "__main__":
    # input_pdf_file = "./sample/gt/Public_257.pdf" 
    # output_md_file = input_pdf_file.replace('.pdf', '.md').replace("gt","pred")
    # pdf_to_markdown_pipeline(input_pdf_file, output_md_file)

    folder_pdf = "./data/var_test/pdf"
    folder_md = "./markdown_pred_opt/"
    
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
    list_pdf = [i for i in os.listdir(folder_pdf) if i.endswith('.pdf')]
    list_pdf.sort()
    for pdf_file in list_pdf:
        input_pdf_file = os.path.join(folder_pdf, pdf_file)
        output_md_file = os.path.join(folder_md, pdf_file.replace('.pdf', '.md'))
        pdf_to_markdown_pipeline(input_pdf_file, output_md_file)