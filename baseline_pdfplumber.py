import pdfplumber
import pandas as pd
import numpy as np

def pdfplumber_table_to_markdown(table):
    """Chuyển đổi đối tượng pdfplumber Table thành chuỗi Markdown."""
    
    # Sử dụng table.extract() để lấy dữ liệu dưới dạng danh sách các hàng
    data = table.extract()
    if not data or not data[0]:
        return ""
    
    # Chuyển đổi sang DataFrame để dễ dàng tạo Markdown
    df = pd.DataFrame(data)
    
    # Thay thế None/NaN bằng chuỗi rỗng
    df = df.replace(r'^\s*$', np.nan, regex=True).fillna('') 
    
    # Chuyển đổi DataFrame thành chuỗi Markdown
    
    if len(df) > 1:
        header = df.iloc[0].astype(str).fillna('')
        df_no_header = df[1:].copy().reset_index(drop=True)
        df_no_header.columns = header
    else:
        # Nếu chỉ có một hàng (chỉ header), tạo DataFrame rỗng với header đó
        header = df.iloc[0].astype(str).fillna('') if len(df) == 1 else []
        df_no_header = pd.DataFrame(columns=header)

    # Thay None/NaN còn lại bằng chuỗi rỗng
    df_no_header = df_no_header.fillna('')

    # Chuyển DataFrame thành Markdown
    markdown_output = df_no_header.to_markdown(index=False)
    return "\n" + markdown_output + "\n\n"
def is_bold(font_name):
    """Kiểm tra xem tên font có chứa từ khóa 'Bold' hoặc 'Black' không."""
    return 'bold' in font_name.lower() or 'black' in font_name.lower()

def is_italic(font_name):
    """Kiểm tra xem tên font có chứa từ khóa 'Italic' hoặc 'Oblique' không."""
    return 'italic' in font_name.lower() or 'oblique' in font_name.lower()

def apply_markdown_formatting(char):
    """Áp dụng định dạng Markdown cho một ký tự dựa trên tên font."""
    font_name = char['fontname']
    text = char['text']
    
    # Kiểm tra In đậm (Bold)
    if is_bold(font_name):
        return f"**{text}**"
    
    # Kiểm tra In nghiêng (Italic)
    elif is_italic(font_name):
        return f"*{text}*"
    
    return text

def get_block_type(obj, table_bboxes):
    """Xác định loại khối (Text hoặc Table) và trả về nội dung/vị trí."""
    
    # Lấy tọa độ Y của đối tượng
    obj_y_top = obj['top']
    obj_y_bottom = obj['bottom']
    
    # Kiểm tra xem khối văn bản có nằm bên trong bất kỳ hộp giới hạn (bbox) nào của bảng không
    for bbox in table_bboxes:
        t_x0, t_top, t_x1, t_bottom = bbox
        
        # Nếu khối văn bản nằm hoàn toàn trong phạm vi Y của bảng, coi nó là trùng lặp
        if t_top <= obj_y_top < t_bottom and t_top < obj_y_bottom <= t_bottom:
             return None # Bỏ qua, vì nó là một phần của bảng
    
    # Nếu không phải là bảng và không nằm trong phạm vi bảng, nó là Văn bản
    return {
        'type': 'text',
        'top': obj_y_top,
        'content': obj['text'].strip()
    }


def pdf_to_markdown_plumber_only(pdf_path, output_path):
    """Chuyển đổi PDF sang Markdown bằng cách ghép nối Text và Table (pdfplumber)."""
    
    markdown_output = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Đang xử lý file: {pdf_path} với {len(pdf.pages)} trang...")
            
            for i, page in enumerate(pdf.pages):
                page_markdown = []
                page_markdown.append(f"\n---\n\n## Trang {i + 1}\n\n")

                # 1. Trích xuất TẤT CẢ các đối tượng Bảng
                tables = page.find_tables()


                # import ipdb; ipdb.set_trace()
                
                # Lưu trữ các hộp giới hạn (bbox) của bảng để lọc văn bản trùng lặp
                table_bboxes = [t.bbox for t in tables]
                print("table_bboxes:", table_bboxes)

                
                # Tạo danh sách các khối Table (đã chuyển sang Markdown)
                table_blocks = []
                for table in tables:
                    table_blocks.append({
                        'type': 'table',
                        'top': table.bbox[1], # Tọa độ top (y1) của bảng
                        'content': pdfplumber_table_to_markdown(table)
                    })
                
                # 2. Trích xuất các Khối Văn bản (words)
                # Sử dụng extract_text_lines() để lấy từng dòng cùng với tọa độ
                text_lines = page.extract_text_lines(T_y_tolerance=3)
                
                # 3. Kết hợp và Lọc Văn bản Trùng lặp
                content_blocks = []
                
                # Xử lý văn bản, loại bỏ các dòng nằm trong bbox của bảng
                for line in text_lines:
                    block = get_block_type(line, table_bboxes)
                    if block and block['content']:
                        content_blocks.append(block)
                
                # Thêm các khối bảng vào danh sách nội dung
                content_blocks.extend(table_blocks)
                
                # 4. Sắp xếp tất cả các khối theo vị trí 'top' (tọa độ Y)
                content_blocks.sort(key=lambda x: x['top'])
                if content_blocks[0]['type'] == 'table' and "VIETTEL AI RACE" in content_blocks[0]['content']:
                    content_blocks = content_blocks[1:]
                if i==4:
                    import ipdb; ipdb.set_trace()   
                # 5. Ghép nối thành chuỗi Markdown
                for block in content_blocks:
                    if block['type'] == 'text':
                        # Thêm logic nhận diện tiêu đề đơn giản tại đây nếu cần (như ví dụ trước)
                        page_markdown.append(block['content'] + "\n")
                    elif block['type'] == 'table':
                        page_markdown.append(block['content'])

                markdown_output.extend(page_markdown)
                
        # Ghi kết quả ra file Markdown
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("".join(markdown_output))
            
        print(f"\n✅ Chuyển đổi thành công! Kết quả đã được lưu tại: {output_path}")

    except Exception as e:
        print(f"❌ Lỗi xảy ra trong quá trình xử lý: {e}")

# --- PHẦN SỬ DỤNG ---
if __name__ == "__main__":
    input_pdf_file = "./sample/gt/Public_064.pdf" 
    output_md_file = input_pdf_file.replace('.pdf', '.md').replace("gt", "pred")
    
    # Đảm bảo file 'input.pdf' tồn tại
    pdf_to_markdown_plumber_only(input_pdf_file, output_md_file)