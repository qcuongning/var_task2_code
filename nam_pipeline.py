import pymupdf4llm
from glob import glob
import os
import re
import fire

# Hàm cũ: Chuyển đổi bảng Markdown thô sang HTML
def convert_pipe_table_to_html(md_text: str) -> str:
    """
    Tìm và chuyển đổi các khối dữ liệu dạng 'pipe table' (|...|) sang bảng HTML cơ bản.
    """
    parts = md_text.split('\n\n')
    output_parts = []
    
    for part in parts:
        # Nếu đoạn bắt đầu bằng '|' và có ít nhất 2 dòng chứa '|', ta xem đó là bảng
        if part.strip().startswith('|') and part.count('\n|') >= 1:
            lines = [line.strip() for line in part.split('\n') if line.strip()]
            
            html = "<table>\n"
            
            # Hàng đầu tiên (header)
            headers = [h.strip() for h in lines[0].strip('|').split('|')]
            html += "<thead>\n<tr>"
            for h in headers:
                html += f"<th>{h}</th>"
            html += "</tr>\n</thead>\n<tbody>"

            # Các hàng còn lại (body)
            for row_line in lines[1:]:
                cells = [c.strip() for c in row_line.strip('|').split('|')]
                if not any(cells) or all(re.match(r'^[\s-]*$', c) for c in cells):
                    continue
                    
                html += "\n<tr>"
                for c in cells:
                    html += f"<td>{c}</td>"
                html += "</tr>"
                
            html += "\n</tbody>\n</table>"
            output_parts.append(html)
        else:
            output_parts.append(part)
            
    return '\n\n'.join(output_parts)

# Hàm MỚI: Loại bỏ bảng tiêu đề ở đầu trang
def remove_initial_header_content(md_text: str) -> str:
    """
    Loại bỏ các dòng/khối nội dung tiêu đề không mong muốn ở đầu tệp Markdown.
    Cơ chế: Loại bỏ các dòng pipe table đơn lẻ, sau đó loại bỏ khối HTML table 
    đầu tiên (chứa thông tin tiêu đề/phiên bản).
    """
    
    # 1. Chuẩn hóa khoảng trắng đầu và cuối
    md_text = md_text.strip()
    
    # 2. Loại bỏ các dòng pipe table header đơn lẻ ở đầu tệp (dạng |...|...)
    # Loại bỏ bất kỳ dòng nào bắt đầu bằng | và có ít nhất 2 dấu |
    # Ta chỉ tập trung loại bỏ ở phần đầu tài liệu.
    pattern_pipe_header = re.compile(r'^\|[^|\n]*\|[^|\n]*\|[^|\n]*\|.*$', re.MULTILINE)
    
    # Áp dụng thay thế lặp lại để loại bỏ các dòng pipe header liên tiếp ở đầu file.
    # Giới hạn lặp để không ảnh hưởng đến phần nội dung.
    for _ in range(5): 
        old_text = md_text
        # Chỉ thay thế lần xuất hiện đầu tiên của dòng pipe table header
        md_text = re.sub(pattern_pipe_header, '', md_text, count=1) 
        if old_text == md_text:
            break
            
    # Dọn dẹp các dòng trống tạo ra
    md_text = re.sub(r'\n\s*\n', '\n\n', md_text).strip()

    # 3. Loại bỏ khối HTML table đầu tiên
    # Tìm khối <table>...</table> đầu tiên ở đầu văn bản.
    pattern_html_table = re.compile(r'^\s*<table>.*?</table>', re.DOTALL)
    
    # Chỉ loại bỏ nếu nó nằm ở đầu tài liệu.
    match = pattern_html_table.match(md_text)
    if match:
        # Cắt bỏ khối <table> và dọn dẹp khoảng trắng
        md_text = md_text[match.end():].strip() 
    
    # Dọn dẹp lại các dòng trống và khoảng trắng thừa cuối cùng
    md_text = re.sub(r'\n\s*\n', '\n\n', md_text).strip()
    
    return md_text

# Hàm cũ: Sửa lỗi ký tự và công thức
def fix_unicode_and_math_errors(md_text: str) -> str:
    """
    Sửa lỗi ký tự unicode và ký tự toán học bị dịch sai (µ, ).
    """
    md_text = md_text.replace('W', '$\mu$W')
    md_text = md_text.replace('V', '$\mu$V')
    md_text = md_text.replace('', '$\mu$')
    md_text = md_text.replace('', '$\leq$')
    md_text = re.sub(r'(\d+)\<', r'\1 <', md_text)
    md_text = re.sub(r'(\d+)\>', r'\1 >', md_text)
    return md_text

# Hàm cũ: Thêm khai báo ngôn ngữ cho code block
def add_language_to_code_blocks(md_text: str, language: str = 'cpp') -> str:
    """
    Tìm các code block (```) không có khai báo ngôn ngữ và thêm ngôn ngữ vào.
    """
    pattern = re.compile(r'^\s*```\s*$', re.MULTILINE)
    return pattern.sub(f'```{language}', md_text)


def transform(pdf_dir: str, md_dir: str):
    """
    Chuyển đổi tất cả các tệp PDF và áp dụng hậu xử lý theo yêu cầu.
    """
    os.makedirs(md_dir, exist_ok=True)
    file_list = glob(f"{pdf_dir}/*.pdf")

    for pdf in file_list:
        print(f"Đang chuyển đổi và xử lý hậu kỳ {os.path.basename(pdf)}...")
        
        # BƯỚC 1: Chuyển đổi PDF sang Markdown thô
        md_text_raw = pymupdf4llm.to_markdown(pdf)
        
        # BƯỚC 2: Hậu xử lý (Post-processing)
        md_text_processed = md_text_raw
        
        # 2.1. Chuyển đổi bảng Markdown thô sang HTML (cần làm trước để khối HTML được tạo)
        md_text_processed = convert_pipe_table_to_html(md_text_processed)
        
        # 2.2. Loại bỏ tiêu đề đầu trang
        md_text_processed = remove_initial_header_content(md_text_processed)
        
        # 2.3. Sửa lỗi ký tự Unicode và Toán học
        md_text_processed = fix_unicode_and_math_errors(md_text_processed)
        
        # 2.4. Thêm khai báo ngôn ngữ cho các code block
        md_text_processed = add_language_to_code_blocks(md_text_processed, language='cpp')
        
        # Ghi nội dung Markdown đã xử lý
        output_filename = os.path.basename(pdf).replace('.pdf', '.md')
        output_filepath = os.path.join(md_dir, output_filename)
        
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(md_text_processed)
        print(f"Đã lưu thành công tới {output_filepath}")
            


if __name__ == "__main__":
    fire.Fire(transform)