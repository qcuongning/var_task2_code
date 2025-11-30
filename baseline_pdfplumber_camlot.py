import pdfplumber
import camelot
import pandas as pd
import numpy as np

def camelot_to_markdown(table):
    """Chuyển đổi đối tượng Camelot Table thành chuỗi Markdown."""
    
    # Chuyển đổi bảng Camelot thành Pandas DataFrame
    df = table.df.replace(r'^\s*$', np.nan, regex=True).fillna('') # Thay thế khoảng trắng bằng chuỗi rỗng
    
    # Chuyển đổi DataFrame thành chuỗi Markdown
    markdown_output = df.to_markdown(index=False)
    return markdown_output + "\n\n"

def pdf_to_markdown_with_camelot(pdf_path, output_path):
    """Sử dụng Camelot để trích xuất bảng, pdfplumber cho văn bản."""
    
    markdown_output = []
    
    try:
        # 1. Trích xuất TẤT CẢ các bảng bằng Camelot (Phương pháp "lattice" hoặc "stream")
        # 'pages='all'' để xử lý tất cả các trang.
        print(f"Bắt đầu trích xuất bảng bằng Camelot từ file: {pdf_path}...")
        tables = camelot.read_pdf(
            pdf_path, 
            pages='all', 
            flavor='lattice', # Dùng 'stream' cho bảng không có đường kẻ, 'lattice' cho bảng có đường kẻ
            split_text=True
        )
        print(f"✅ Camelot trích xuất được {tables.n} bảng.")
        
        # Tạo danh sách các bảng Markdown đã trích xuất
        camelot_markdown_tables = [camelot_to_markdown(table) for table in tables]

        # 2. Trích xuất Văn bản và ghép nối bằng pdfplumber
        print("Bắt đầu trích xuất văn bản bằng pdfplumber...")
        with pdfplumber.open(pdf_path) as pdf:
            
            for i, page in enumerate(pdf.pages):
                page_markdown = []
                page_markdown.append(f"\n---\n\n## Trang {i + 1}\n\n")

                # Trích xuất văn bản thô theo layout
                text = page.extract_text(layout=True)
                
                # --- Lược bỏ văn bản trùng lặp (các bảng đã trích xuất) ---
                # Đây là phần phức tạp nhất. Để đơn giản hóa, ta TÁCH bảng và văn bản.
                # Cách tiếp cận đơn giản: Lấy toàn bộ văn bản rồi chèn bảng vào vị trí ước lượng.
                
                # CÁCH ĐƠN GIẢN NHẤT: Trích xuất toàn bộ văn bản rồi chèn tất cả các bảng Camelot vào cuối mỗi trang.
                # (Với các ứng dụng RAG/LLM, việc phân mảnh dữ liệu quan trọng hơn vị trí chính xác)
                
                # 2.1. Trích xuất văn bản
                stripped_text = text.strip() if text else ""
                if stripped_text:
                    # Có thể thêm logic nhận diện tiêu đề tại đây (như ví dụ trước)
                    page_markdown.append(stripped_text + "\n\n")
                
                # 2.2. Chèn các bảng Camelot của trang hiện tại (Dựa trên chỉ mục trang)
                # Chỉ chèn các bảng Camelot thuộc về trang này
                page_tables_md = [
                    camelot_to_markdown(table) 
                    for table in tables 
                    if table.page == i + 1 # Camelot bắt đầu đếm trang từ 1
                ]
                
                if page_tables_md:
                    page_markdown.append("\n### Bảng dữ liệu\n\n")
                    page_markdown.extend(page_tables_md)
                
                markdown_output.extend(page_markdown)
        
        # Ghi kết quả ra file Markdown
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("".join(markdown_output))
            
        print(f"\n✅ Chuyển đổi thành công! Kết quả đã được lưu tại: {output_path}")

    except Exception as e:
        print(f"❌ Lỗi xảy ra trong quá trình xử lý: {e}")

# --- PHẦN SỬ DỤNG ---
if __name__ == "__main__":
    input_pdf_file = "./data/var_train/pdf/Public_064.pdf" 
    output_md_file = "output_camelot.md"
    
    # Đảm bảo file 'input.pdf' tồn tại
    pdf_to_markdown_with_camelot(input_pdf_file, output_md_file)

