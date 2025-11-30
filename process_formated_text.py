import pdfplumber

def is_bold(font_name):
    """Kiểm tra xem tên font có chứa từ khóa 'Bold' hoặc 'Black' không."""
    return 'bold' in font_name.lower() or 'black' in font_name.lower()

def is_italic(font_name):
    """Kiểm tra xem tên font có chứa từ khóa 'Italic' hoặc 'Oblique' không."""
    return 'italic' in font_name.lower() or 'oblique' in font_name.lower()

def get_word_format_type(font_name):
    """Xác định loại định dạng: 'bold', 'italic', hay 'none'."""
    if is_bold(font_name):
        return 'bold'
    if is_italic(font_name):
        return 'italic'
    return 'none'

def extract_and_format_page(page):
    """Trích xuất và định dạng văn bản trang theo từng từ."""
    chars = page.chars
    words = page.extract_words()
    
    formatted_words = []
    
    for word in words:
        word_chars = [c for c in chars 
                      if c['x0'] >= word['x0'] and c['x1'] <= word['x1'] and 
                         c['top'] >= word['top'] and c['bottom'] <= word['bottom']]
        
        if word_chars:
            first_char_font = word_chars[0]['fontname']
            format_type = get_word_format_type(first_char_font)
        else:
            format_type = 'none'

        formatted_words.append({
            'text': word['text'],
            'type': format_type,
            'top': word['top'], # Giữ lại tọa độ để xác định ngắt dòng
            'bottom': word['bottom']
        })
        
    return formatted_words

def merge_formatted_blocks(formatted_words):
    """Ghép nối các từ có cùng định dạng liền kề."""
    if not formatted_words:
        return ""
    
    merged_output = []
    current_block = None
    
    for i, word in enumerate(formatted_words):
        # Xác định xem từ này có nằm trên cùng một dòng với từ trước đó không
        is_same_line = (i > 0 and abs(word['top'] - formatted_words[i-1]['top']) < 3)
        
        if current_block is None:
            # Bắt đầu khối đầu tiên
            current_block = {'type': word['type'], 'words': [word['text']]}
            continue
        
        # 1. Kiểm tra ngắt dòng
        if not is_same_line:
            # Nếu là ngắt dòng, xử lý khối hiện tại và bắt đầu khối mới
            merged_output.append(process_block(current_block))
            # Thêm ngắt dòng Markdown (hai dấu cách + ngắt dòng)
            merged_output.append("  \n") 
            current_block = {'type': word['type'], 'words': [word['text']]}
            continue
        
        # 2. Kiểm tra định dạng liền kề (trên cùng một dòng)
        if word['type'] == current_block['type']:
            # Nếu cùng định dạng, thêm từ vào khối hiện tại
            current_block['words'].append(word['text'])
        else:
            # Nếu định dạng thay đổi, xử lý khối hiện tại và bắt đầu khối mới
            merged_output.append(process_block(current_block))
            current_block = {'type': word['type'], 'words': [word['text']]}
    
    # Xử lý khối cuối cùng sau khi vòng lặp kết thúc
    if current_block:
        merged_output.append(process_block(current_block))
        
    return "".join(merged_output)

import re

def process_block(block):
    """
    Gói một khối văn bản bằng dấu Markdown thích hợp, 
    ưu tiên nhận diện Tiêu đề có thứ tự (1. 2. ...) nếu là in đậm.
    """
    # Ghép nối các từ trong khối thành một chuỗi
    text = " ".join(block['words'])
    
    # Biểu thức chính quy: Kiểm tra xem chuỗi có bắt đầu bằng một hoặc nhiều chữ số, 
    # theo sau là dấu chấm và một khoảng trắng không.
    # ^: bắt đầu chuỗi
    # \d+: một hoặc nhiều chữ số
    # \.: dấu chấm (cần escape)
    # \s: khoảng trắng
    ordered_list_pattern = re.compile(r"^\d+\.\s")
    
    # 1. Kiểm tra Tiêu đề có thứ tự (chỉ kiểm tra nếu định dạng gốc là 'bold')
    if block['type'] == 'bold' and ordered_list_pattern.match(text):
        # Nếu là in đậm VÀ bắt đầu bằng 1., 2., ..., coi nó là Tiêu đề/Mục lớn.
        # Ở đây ta sử dụng # (H1) để làm nổi bật tiêu đề.
        # Lưu ý: Cú pháp Markdown cho Danh sách có thứ tự đã là 1. Item.
        # Việc thêm # sẽ biến nó thành tiêu đề H1, tùy thuộc vào cách bạn muốn thể hiện.
        
        # Nếu muốn biến thành Tiêu đề H1:
        return re.sub(ordered_list_pattern, "# ", text, count=1)
        
        # HOẶC, nếu bạn chỉ muốn giữ nguyên 1. 2. mà KHÔNG GÓI nó bằng ** **:
        # return text 
        
    # 2. Xử lý định dạng In đậm thông thường
    elif block['type'] == 'bold':
        return f"**{text}**"
        
    # 3. Xử lý định dạng In nghiêng
    elif block['type'] == 'italic':
        return f"*{text}*"
        
    # 4. Định dạng None (thông thường)
    else:
        return text


def pdf_to_formatted_markdown(pdf_path, output_path):
    """Hàm chính để trích xuất, định dạng và ghép nối văn bản."""
    
    markdown_content = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                # 1. Trích xuất văn bản đã định dạng theo từng từ
                formatted_words = extract_and_format_page(page)
                
                # 2. Ghép nối các từ có định dạng liền kề
                page_markdown = merge_formatted_blocks(formatted_words)
                
                markdown_content.append(f"## Trang {i + 1}\n\n")
                markdown_content.append(page_markdown)
                markdown_content.append("\n\n---\n\n")

        # Ghi kết quả
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(markdown_content))
            
        print(f"✅ Đã trích xuất và lưu văn bản đã ghép nối định dạng vào: {output_path}")

    except Exception as e:
        print(f"❌ Lỗi xảy ra: {e}")

# --- PHẦN SỬ DỤNG ---
if __name__ == '__main__':
    input_pdf_file = "./data/var_train/pdf/Public_064.pdf" 
    output_md_file = "formatted_output.md"
    
    pdf_to_formatted_markdown(input_pdf_file, output_md_file)