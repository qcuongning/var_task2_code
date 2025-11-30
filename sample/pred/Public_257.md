# Public_257

*Căn cứ Luật giao dịch điện tử ngày 22 tháng 06 năm 2023;* 


*Căn cứ Nghị định số 23/2025/NĐ-CP ngày 21 tháng 02 năm 2025 của* 


*Chính phủquy định về chữ ký điện tử và dịch vụ tin cậy;* 


*Căn cứ Nghị định số 55/2025/NĐ-CP ngày 02 tháng 3 năm 2025 của Chính* 


*phủ quy định chức năng, nhiệm vụ và cơ cấu tổ chức của Bộ Khoa học và Công* 


*nghệ;* 


*Theo đề nghị của Vụ trưởng Vụ Pháp chế và Giám đốc Trung tâm Chứng* 


*thực điện tử quốc gia;* 


*Bộ trưởng Bộ Khoa học và Công nghệ ban hành Thông tư quy định yêu cầu* 


*kỹ thuật đối với phần mềm ký số, phần mềm kiểm tra chữ ký số và Cổng kết nối* 


*dịch vụ chứng thực chữ ký số công cộng.* 


# 1. QUY ĐỊNH CHUNG


## 1.1. Phạm vi điều chỉnh


Thông tư này quy định yêu cầu kỹ thuật đối với phần mềm ký số, phần mềm


kiểm tra chữ ký số và Cổng kết nối dịch vụ chứng thực chữ ký số công cộng.


## 1.2 . Đối tượng áp dụng


Thông tư này áp dụng đối với tổ chức, cá nhân sử dụng phần mềm ký số,


phần mềm kiểm tra chữ ký số; các tổ chức, cá nhân phát triển phần mềm ký số,


phần mềm kiểm tra chữ ký số; các tổ chức cung cấp dịch vụ chứng thực chữ ký


số; các tổ chức cung cấp dịch vụ chứng thực chữ ký điện tử chuyên dùng đảm bảo


an toàn; các tổ chức cung cấp dịch vụ chứng thực chữ ký điện tử nước ngoài được


công nhận tại Việt Nam; chủ quản các hệ thống thông tin phục vụ giao dịch điện


tử có sử dụng chữ ký số và các tổ chức, cá nhân có liên quan khác.
## 1.3. Giải thích từ ngữ


Trong Thông tư này, các từ ngữ dưới đây được hiểu như sau:


- “Cặp khóa bất đối xứng” là khóa công khai và khóa bí mật tương ứng.


- “Khóa bí mật” là thành phần của cặp khóa bất đối xứng được sử dụng để


ký thông điệp dữ liệu.


- “Khóa công khai” là thành phần của cặp khóa bất đối xứng được sử dụng


để xác thực chữ ký số trên thông điệp dữ liệu.


- “Chủ thể ký” là cá nhân hoặc tổ chức sở hữu chứng thư chữ ký số và sử


dụng khóa bí mật tương ứng để thực hiện ký số trên thông điệp dữ liệu.


- “Chứng thư chữ ký số” là một dạng chứng thư điện tử do tổ chức cung


cấp dịch vụ chứng thực chữ ký số cấp nhằm cung cấp thông tin về khóa công khai


của một cá nhân, tổ chức từ đó xác nhận cá nhân, tổ chức là chủ thể ký thông qua


việc sử dụng khóa bí mật tương ứng.


- “Phần mềm ký số” là chương trình độc lập hoặc một thành phần (module)


phần mềm hoặc giải pháp có chức năng ký số vào thông điệp dữ liệu.


- "Phần mềm kiểm tra chữ ký số" là chương trình độc lập hoặc một thành


phần (module) phần mềm hoặc giải pháp có chức năng kiểm tra tính hợp lệ của


chữ ký số trên thông điệp dữ liệu đã ký.


- "Đường dẫn tin cậy của chứng thư chữ ký số" là thông tin đường dẫn trên


chứng thư chữ ký số xác thực tổ chức cung cấp dịch vụ chứng thực chữ ký số đã


cấp phát ra chứng thư chữ ký số đó.


# 2. Yêu cầu kỹ thuật đối với chức năng phần mềm ký số, phần mềm kiểm tra


**chữ ký số** 


## 2.1 Yêu cầu chung


Tuân thủ các yêu cầu và tiêu chuẩn kỹ thuật về chữ ký số trên thông điệp


dữ liệu tại Phụ lục I ban hành kèm theo Thông tư này.
## 2.2 Yêu cầu về chức năng


- Chức năng xác thực chủ thể ký và ký số:


+ Kiểm tra được thông tin chủ thể ký trên chứng thư chữ ký số;


+ Cho phép chủ thể ký sử dụng khóa bí mật để thực hiện việc ký số vào


thông điệp dữ liệu. Khoá bí mật lưu trong thiết bị được chủ thể ký sử dụng để ký


số phải tuân thủ các yêu cầu và tiêu chuẩn kỹ thuật tại Phụ lục I ban hành kèm


theo Thông tư này;


+ Cho phép chuyển đổi định dạng thông điệp dữ liệu thành các định dạng


được nêu tại Phụ lục I ban hành kèm theo Thông tư này;


+ Gắn kèm chữ ký số và chứng thư chữ ký số vào thông điệp dữ liệu sau


khi ký số;


+ Hỗ trợ cài đặt, tích hợp chứng thư chữ ký số của Tổ chức cung cấp dịch


vụ chứng thực chữ ký số quốc gia và chứng thư chữ ký số thuộc Danh sách tin


cậy chứng thư chữ ký điện tử nước ngoài được công nhận tại Việt Nam;


+ Đáp ứng các giao thức gửi nhận thông điệp dữ liệu của phần mềm ký số


theo các yêu cầu và tiêu chuẩn tại Phụ lục I ban hành kèm theo Thông tư này.


- Chức năng kiểm tra hiệu lực của chứng thư chữ ký số:


+ Thông tin trong chứng thư chữ ký số được định danh theo quy định pháp


luật về định danh và xác thực điện tử;


+ Chứng thư chữ ký số của chủ thể ký phải được kiểm tra theo đường dẫn


tin cậy của chứng thư chữ ký số đó và phải liên kết đến chứng thư chữ ký số gốc


của Tổ chức cung cấp dịch vụ chứng thực chữ ký số quốc gia hoặc thuộc Danh


sách tin cậy chứng thư chữ ký điện tử nước ngoài được công nhận tại Việt Nam;


+ Chứng thư chữ ký số phải có hiệu lực tại thời điểm ký số và đáp ứng các


tiêu chí tại Phụ lục II ban hành kèm theo Thông tư này.


- Chức năng kết nối đến Cổng kết nối dịch vụ chứng thực chữ ký số công


cộng: Hướng dẫn kết nối được quy định tại Chương III Thông tư này.
- Chức năng lưu trữ và hủy bỏ các thông tin kèm theo thông điệp dữ liệu ký


số, bao gồm:


+ Chứng thư chữ ký số tương ứng với khóa bí mật mà chủ thể ký sử dụng


để ký thông điệp dữ liệu tại thời điểm ký số;


+ Danh sách chứng thư chữ ký số thu hồi tại thời điểm ký trong chứng thư


chữ ký số của chủ thể ký;


+ Quy chế chứng thực của tổ chức cung cấp dịch vụ chứng thực chữ ký số


đã cấp chứng thư chữ ký số tương ứng với chữ ký số trên thông điệp dữ liệu;


+ Kết quả kiểm tra trạng thái chứng thư chữ ký số tương ứng với chữ ký số


trên thông điệp dữ liệu đã ký.


- Chức năng thay đổi (thêm, bớt) chứng thư chữ ký số của cơ quan, tổ chức


tạo lập cấp, phát hành chứng thư chữ ký số:


Cho phép tích hợp và hiển thị đầy đủ các tổ chức cung cấp dịch vụ chứng


thực chữ ký số và Danh sách tin cậy chứng thư chữ ký điện tử nước ngoài được


công nhận tại Việt Nam.


- Chức năng thông báo bằng chữ hoặc ký hiệu cho chủ thể ký biết việc ký


số vào thông điệp dữ liệu thành công hay không thành công, bao gồm việc:


+ Hiển thị thông báo ký số thành công hoặc không thành công;


+ Xem được thông điệp dữ liệu đã ký sau khi hoàn thành ký số;


+ Tải được thông điệp dữ liệu đã ký về thiết bị.


## 2.3 Yêu cầu chung


Tuân thủ các yêu cầu và tiêu chuẩn kỹ thuật về chữ ký số trên thông điệp


dữ liệu tại Phụ lục I ban hành kèm theo Thông tư này.


## 2.4 Yêu cầu về chức năng


- Chức năng kiểm tra tính hợp lệ của chữ ký số trên thông điệp dữ liệu:
+ Cho phép xác thực chữ ký số trên thông điệp dữ liệu theo nguyên tắc chữ


ký số được tạo ra đúng với khóa bí mật tương ứng với khóa công khai trên chứng


thư chữ ký số;


+ Cho phép kiểm tra chứng thư chữ ký số của chủ thể ký theo đường dẫn


tin cậy của chứng thư chữ ký số đó và phải liên kết đến Tổ chức cung cấp dịch vụ


chứng thực chữ ký số quốc gia hoặc thuộc Danh sách tin cậy chứng thư chữ ký


điện tử nước ngoài được công nhận tại Việt Nam;


+ Bảo đảm chứng thư chữ ký số phải có hiệu lực tại thời điểm ký số và đáp


ứng các tiêu chí tại Phụ lục II ban hành kèm theo Thông tư này;


+ Cho phép kiểm tra tính toàn vẹn của thông điệp dữ liệu ký số theo các


bước sau:


- Giải mã chữ ký số trên thông điệp dữ liệu để có thông tin về mã băm của


thông điệp dữ liệu;


- Sử dụng thuật toán hàm băm an toàn đã tạo ra mã băm trên chữ ký số để


thực hiện tạo mã băm cho thông điệp dữ liệu;


- So sánh sự trùng khớp của hai mã băm để kiểm tra tính toàn vẹn của thông


điệp dữ liệu ký số.


+ Đảm bảo tính hợp lệ của chữ ký số trên thông điệp dữ liệu đã ký theo các


tiêu chí tại Phụ lục II ban hành kèm theo Thông tư này;


+ Hỗ trợ cài đặt, tích hợp chứng thư chữ ký số của Tổ chức cung cấp dịch


vụ chứng thực chữ ký số quốc gia và chứng thư chữ ký số thuộc danh sách tin cậy


chứng thư chữ ký điện tử nước ngoài được công nhận tại Việt Nam;


+ Đáp ứng các giao thức gửi nhận thông điệp dữ liệu của phần mềm ký số


theo tiêu chuẩn tại Phụ lục I ban hành kèm theo Thông tư này.


- Chức năng lưu trữ và hủy bỏ các thông tin kèm theo thông điệp dữ liệu ký


số:
+ Chứng thư chữ ký số tương ứng với chữ ký số trên thông điệp dữ liệu đã


ký;


+ Danh sách chứng thư chữ ký số thu hồi tại thời điểm ký được thể hiện


trong chứng thư chữ ký số đính kèm thông điệp dữ liệu đã ký;


+ Quy chế chứng thực của các tổ chức cung cấp dịch vụ chứng thực chữ ký


số cấp phát chứng thư chữ ký số tương ứng với các chữ ký số trên thông điệp dữ


liệu đã ký;


+ Kết quả kiểm tra trạng thái chứng thư chữ ký số tương ứng với chữ ký số


trên thông điệp dữ liệu đã ký.


- Chức năng thay đổi (thêm, bớt) chứng thư chữ ký số của cơ quan, tổ chức


tạo lập, cấp, phát hành chứng thư chữ ký số.


- Chức năng thông báo bằng chữ hoặc ký hiệu việc kiểm tra tính hợp lệ của


chữ ký số là hợp lệ hay không hợp lệ:


+ Hiển thị thông báo chữ ký số trên thông điệp dữ liệu đã ký hợp lệ hay


không hợp lệ;


+ Hiển thị các thông tin về chữ ký số và chứng thư chữ ký số trên thông


điệp dữ liệu đã ký, với tối thiểu các trường thông tin sau: thông tin về cơ quan, tổ


chức tạo lập, cấp, phát hành chứng thư chữ ký số; thông tin về chủ thể ký; thông


tin về thời điểm ký số hoặc dấu thời gian (nếu có); tính toàn vẹn của thông điệp


dữ liệu đã ký; tính hợp lệ của chữ ký số tại thời điểm ký.


# 3. CỔNG KẾT NỐI DỊCH VỤ CHỨNG THỰC CHỮ KÝ SỐ CÔNG


**CỘNG** 


## 3.1 Cổng kết nối dịch vụ chứng thực chữ ký số công cộng


Cổng kết nối dịch vụ chứng thực chữ ký số công cộng là hệ thống thông tin


phục vụ kết nối dịch vụ chứng thực chữ ký số công cộng với các hệ thống thông


tin phục vụ giao dịch điện tử sử dụng chữ ký số để bảo đảm tính xác thực, tính


toàn vẹn và tính chống chối bỏ của thông điệp dữ liệu.
## 3.2 Kết nối đến Cổng kết nối dịch vụ chứng thực chữ ký số công cộng


- Các tổ chức cung cấp dịch vụ chứng thực chữ ký số công cộng kết nối đến


Cổng kết nối dịch vụ chứng thực chữ ký số công cộng, cụ thể:


+ Thực hiện theo Hướng dẫn kết nối tại Phụ lục III ban hành kèm theo


Thông tư này;


+ Cung cấp các đặc tả, thông số kỹ thuật và thông tin phục vụ kết nối cho


Tổ chức cung cấp dịch vụ chứng thực điện tử quốc gia;


+ Cập nhật các thông số kỹ thuật hoặc thông tin phục vụ kết nối khi có thay


đổi cho Tổ chức cung cấp dịch vụ chứng thực điện tử quốc gia.


- Các hệ thống thông tin phục vụ giao dịch điện tử sử dụng chữ ký số tích


hợp với Cổng kết nối dịch vụ chứng thực chữ ký số công cộng để bảo đảm tính


xác thực, tính toàn vẹn và tính chống chối bỏ của thông điệp dữ liệu, cụ thể:


+ Thực hiện theo Hướng dẫn kết nối tại Phụ lục III ban hành kèm theo


Thông tư này;


+ Bảo đảm chức năng ký số của hệ thống thông tin phục vụ giao dịch điện


tử sử dụng chữ ký số đáp ứng các quy định tại Điều 5 Thông tư này;


+ Tổ chức cung cấp dịch vụ chứng thực điện tử quốc gia cung cấp các đặc


tả, thông số kỹ thuật và thông tin phục vụ việc kết nối đến Cổng kết nối dịch vụ


chứng thực chữ ký số công cộng.


- Đầu mối hỗ trợ, hướng dẫn kết nối đến Cổng kết nối dịch vụ chứng thực


chữ ký số công cộng: Trung tâm Chứng thực điện tử quốc gia, Bộ Khoa học và


Công nghệ.
# 4. ĐIỀU KHOẢN THI HÀNH


## 4.1 Tổ chức thực hiện


- Trung tâm Chứng thực điện tử quốc gia có trách nhiệm hướng dẫn thực


hiện các nội dung của Thông tư này và công bố thông tin theo quy định tại điểm


c khoản 2 Điều 9 Thông tư này.


- Tổ chức cung cấp dịch vụ chứng thực chữ ký số công cộng, tổ chức cung


cấp dịch vụ chứng thực chữ ký điện tử chuyên dùng đảm bảo an toàn, Tổ chức


cung cấp dịch vụ chứng thực chữ ký điện tử nước ngoài được công nhận tại Việt


Nam có trách nhiệm công bố các đặc tả kỹ thuật (tài liệu và bộ công cụ), chứng


thư chữ ký số liên quan đến tổ chức cung cấp dịch vụ chứng thực chữ ký số và


các tiêu chuẩn chữ ký số trên trang tin điện tử của tổ chức cung cấp dịch vụ chứng


thực chữ ký số đó.


- Tổ chức, cá nhân phát triển, sử dụng phần mềm ký số, phần mềm kiểm tra


chữ ký số có trách nhiệm tuân thủ các quy định về yêu cầu kỹ thuật, hướng dẫn


sử dụng đối với phần mềm ký số, phần mềm kiểm tra chữ ký số.


## 4.2 Hiệu lực thi hành


- Thông tư này có hiệu lực thi hành kể từ ngày tháng năm .


- Chánh Văn phòng, Giám đốc Trung tâm Chứng thực điện tử quốc gia, Thủ


trưởng các cơ quan, đơn vị thuộc Bộ, Giám đốc Sở Khoa học và Công nghệ các


tỉnh, thành phố trực thuộc Trung ương, tổ chức, cá nhân có liên quan chịu trách


nhiệm thi hành Thông tư này.


- Trong quá trình thực hiện, nếu có khó khăn, vướng mắc, cơ quan, tổ chức,


cá nhân phản ánh kịp thời về Bộ Khoa học và Công nghệ (Trung tâm Chứng thực


điện tử quốc gia) để xem xét, giải quyết./.



**Phụ lục I** 


**DANH MỤC TIÊU CHUẨN KỸ THUẬT VỀ CHỮ KÝ SỐ** 


**TRÊN THÔNG ĐIỆP DỮ LIỆU DÙNG CHO PHẦN MỀM KÝ SỐ VÀ** 


**PHẦN MỀM KIỂM TRA CHỮ KÝ SỐ** 


*(Ban hành kèm theo Thông tư số /2025/TT-BKHCN ngày tháng năm 2025 của Bộ* 


*trưởng Bộ Khoa học và Công nghệ)* 



<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Số TT</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Loại tiêu</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Ký hiệu</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Tên đầy đủ của tiêu</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Quy định áp</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chuẩn</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>tiêu chuẩn</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chuẩn</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Tiêu chuẩn về định dạng thông điệp dữ liệu</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>11</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Bộ ký tự và
mã hóa</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ASCII</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>American Standard Code</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp
dụng</p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>for Information</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Interchange</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>12</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Bộ ký tự và</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>TCVN
6909:2001</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>TCVN 6909:2001 “ Công</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Bắt buộc áp
dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>mã hóa cho</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>nghệ thông tin-Bộ mã ký</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>tiếng Việt</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>tự tiếng Việt 16-bit”</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>13</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Trình diễn bộ
ký tự</p></blockquote></td>
<td><blockquote><p>Trình diễn bộ</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>UTF-8</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>8-bit Universal</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp
dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ký tự</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Character Set (UCS)/</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Unicode Transformation</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Format</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>14</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Ngôn ngữ
định dạng
thông điệp
dữ liệu</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>XML v1.0</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Extensible Markup
Language version 1.0
(5th Edition)</p></blockquote></td>
<td><blockquote><p>Extensible Markup</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp
dụng một trong
hai tiêu chuẩn</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Language version 1.0</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>(5th</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>(5th Edition)</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Edition)</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>XML v1.1</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Extensible Markup
Language version 1.1</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>(2nd</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Edition)</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Bộ ký tự và</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>mã hóa</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>TCVN</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>6909:2001</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Bắt buộc áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Khuyến nghị áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Ngôn ngữ</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>định dạng</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>thông điệp</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>dữ liệu</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Khuyến nghị áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng một trong</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>hai tiêu chuẩn</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Extensible Markup</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>Language version 1.1</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>15</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Định nghĩa</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>XML
Schema
version 1.1</strong></p></blockquote></th>
<th><blockquote><p><strong>XML Schema version 1.1</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Khuyến nghị áp
dụng</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>các lược đồ</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>trong tài liệu</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>XML</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>16</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Trao đổi dữ</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>XML v2.4.2</p></blockquote></td>
<td><blockquote><p>XML Metadata
Interchange version 2.4.2</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp
dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>liệu đặc tả</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>tài liệu XML</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>77</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Quản lý tài</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ISO 32000-
1:2008</p></blockquote></td>
<td><blockquote><p>Document management -
Portable document
format</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp
dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>liệu - Định</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dạng tài liệu</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>di động</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>88</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Định dạng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>RFC7159</p></blockquote></td>
<td><blockquote><p>The JavaScript Object
Notation (JSON) Data
Interchange Format</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp
dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>trao đổi dữ</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>liệu theo ký</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>hiệu đối</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>tượng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Javascript</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Tiêu chuẩn về ký số, kiểm tra chữ ký số</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>21</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Tiêu chuẩn về ký số trên thiết bị quản lý khóa bí mật, phần mềm</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ký số, tạo chữ ký số, chứng thư số, phần mềm kiểm tra chữ ký số.</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>21.1</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Thuật toán
mã hóa</p></blockquote></td>
<td><blockquote><p>Thuật toán</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>TCVN
7816:2007</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Công nghệ thông tin. Kỹ</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp
dụng</p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>mã hóa</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>thuật mật mã - thuật toán</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>mã dữ liệu AES</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>NIST 800-
67</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Recommendation for the</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp
dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Triple Data Encryption</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Algorithm (TDEA) Block</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Cipher</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>XML</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>Schema</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>version 1.1</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Khuyến nghị áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>XML Metadata</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>Interchange version 2.4.2</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Khuyến nghị áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>ISO 32000-</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>1:2008</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Document management -</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>Portable document</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>format</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Khuyến nghị áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>The JavaScript Object</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>Notation (JSON) Data</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>Interchange Format</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Khuyến nghị áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>TCVN</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>7816:2007</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>NIST 800-</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>67</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Khuyến nghị áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>PKCS#1</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>RSA Cryptography</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Khuyến nghị áp
dụng</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Standard (Phiên bản 2.1</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>trở lên)</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Áp dụng, sử dụng lược</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>đồ RSAES-OAEP để mã</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>hoá</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Độ dài khóa tối thiểu là</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>2048 bit</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ECC</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Elliptic Curve</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Crytography</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>21.2</p></blockquote></td>
<td><blockquote><p>Thuật toán
chữ ký số</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>TCVN</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Các kỹ thuật mật mã -</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>- Áp dụng một</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>7635:2007</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Chữ ký số</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>trong ba tiêu</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chuẩn.</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>PKCS#1</p></blockquote></td>
<td><blockquote><p>PKCS#1</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>RSA Cryptography</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>- Đối với tiêu</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Standard</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chuẩn TCVN</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ANSI
X9.62-2005</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Public Key Cryptography
for the Financial
Services Industry: The
Elliptic Curve Digital
Signature Algorithm
(ECDSA)</p></blockquote></td>
<td><blockquote><p>Public Key Cryptography</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>7635:2007 và</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>PKCS#1:</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>for the Financial</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Services Industry: The</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>+ Phiên bản 2.1</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Elliptic Curve Digital</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>+ Áp dụng lược</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Signature Algorithm</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>đồ RSAES-</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>(ECDSA)</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>OAEP để mã</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>hoá và RSASSA-</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>PSS để ký.</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>+ Độ dài khóa</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>tối thiểu là 2048</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>bit</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>- Đối với tiêu</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chuẩn ECDSA:</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>độ dài khóa tối</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>thiểu là 256 bit</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Khuyến nghị áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Thuật toán</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>chữ ký số</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>ANSI</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>X9.62-2005</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>21.3</strong></p></blockquote></th>
<th><blockquote><p><strong>Hàm băm an
toàn</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>FIPS PUB</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Secure Hash Algorithms</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Áp dụng một</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>180-4</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>trong các hàm</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>băm sau:</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>FIPS PUB
202</p></blockquote></td>
<td><blockquote><p>FIPS PUB</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHA-3 Standard:
Permutation-Based Hash
and Extendable-Output
Functions</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHA-224,</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>202</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHA-256,</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHA-384,</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHA-512,</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHA-512/224,</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHA-512/256,</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHA3-224,</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHA3-256,</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHA3-384,</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHA3-512,</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHAKE128,</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>SHAKE256</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>21.4</p></blockquote></td>
<td><blockquote><p>Cú pháp mã
hóa và cách
xử lý thông
điệp dữ liệu
định dạng
XML</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>XML</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>XML Encryption Syntax
and Processing</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp
dụng</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Encryption</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Syntax and</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Processing</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>XML</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>XML Signature Syntax
and Processing</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp
dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Signature</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Syntax and</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Processing</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>21.5</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Quản lý khóa</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>XKMS v2.0</p></blockquote></td>
<td><blockquote><p>XKMS v2.0</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>XML Key Management
Specification version 2.0</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp
dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>công khai</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>thông điệp</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dữ liệu định</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dạng XML</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>21.6</p></blockquote></td>
<td><blockquote><p>Cú pháp
thông điệp</p></blockquote></td>
<td><blockquote><p>Cú pháp</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>PKCS#7</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Cryptographic message
syntax for file-based</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp
dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>thông điệp</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>v1.5 (RFC</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>2315)</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Hàm băm an</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>toàn</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>SHA-3 Standard:</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>Permutation-Based Hash</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>and Extendable-Output</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>Functions</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Cú pháp mã</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>hóa và cách</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>xử lý thông</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>điệp dữ liệu</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>định dạng</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>XML</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>XML Encryption Syntax</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>and Processing</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>XML Signature Syntax</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>and Processing</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Bắt buộc áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>XML Key Management</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>Specification version 2.0</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Bắt buộc áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Cryptographic message</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>syntax for file-based</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Bắt buộc áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>mật mã cho</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>signing and encrypting</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ký, mã hóa</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>version 1.5</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>11.7</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Tiêu chuẩn</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ETSI EN
319 142-1</p></blockquote></td>
<td><blockquote><p>Electronic Signatures
and Infrastructures (ESI)
- PAdES digital
signatures</p></blockquote></td>
<td><blockquote><p>Electronic Signatures</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Áp dụng một
trong hai tiêu
chuẩn PAdES
hoặc CAdES</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>về chữ ký</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>and Infrastructures (ESI)</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>điện tử nâng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>- PAdES digital</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>cao dành cho</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>signatures</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>thông điệp</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dữ liệu định</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dạng PDF</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>11.8</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Tiêu chuẩn</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ETSI TS
101 903</p></blockquote></td>
<td><blockquote><p>Electronic Signatures
and Infrastructures (ESI)
- XML Advanced
Electronic Signatures
(XAdES)</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Áp dụng một
trong hai tiêu
chuẩn XAdES
hoặc CAdES</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>về chữ ký</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>điện tử nâng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>cao dành cho</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>thông điệp</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dữ liệu định</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dạng XML</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>11.9</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Tiêu chuẩn</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>RFC 7515</p></blockquote></td>
<td><blockquote><p>JSON Web Signature
(JWS)</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Bắt buộc áp
dụng cho thông
điệp dữ liệu định
dạng JSON</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>về chữ ký</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>điện tử nâng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>cao dành cho</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>thông điệp</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dữ liệu định</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dạng JSON</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>11.10</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Tiêu chuẩn</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ETSI TS
101 733</p></blockquote></td>
<td><blockquote><p>Electronic Signatures
and Infrastructures (ESI)
- CMS Advanced
Electronic Signatures
(CAdES)</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp
dụng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>về chữ ký</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>điện tử nâng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>cao dành cho</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>cú pháp tin</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>nhắn mật mã</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>.2</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Tiêu chuẩn về hệ thống, thiết bị lưu trữ và sử dụng khóa bí mật</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>ETSI EN</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>319 142-1</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Áp dụng một</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>trong hai tiêu</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>chuẩn PAdES</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>hoặc CAdES</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>ETSI TS</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>101 903</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Electronic Signatures</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>and Infrastructures (ESI)</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>- XML Advanced</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>Electronic Signatures</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>(XAdES)</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Áp dụng một</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>trong hai tiêu</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>chuẩn XAdES</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>hoặc CAdES</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>JSON Web Signature</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>(JWS)</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Bắt buộc áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng cho thông</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>điệp dữ liệu định</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>dạng JSON</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>ETSI TS</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>101 733</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Electronic Signatures</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>and Infrastructures (ESI)</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>- CMS Advanced</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>Electronic Signatures</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>(CAdES)</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Khuyến nghị áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>22.1</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Yêu cầu an</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>FIPS PUB
140-2</strong></p></blockquote></th>
<th><blockquote><p><strong>Security Requirements
for Cryptographic
Modules</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>- Yêu cầu tối
thiểu mức 3
(level 3)</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>toàn dành</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>cho mô đun</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>bảo mật</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>phần cứng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>22.2</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Yêu cầu an</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>FIPS PUB
140-2</p></blockquote></td>
<td><blockquote><p>Security Requirements
for Cryptographic
Modules</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>- Yêu cầu tối
thiểu mức 2
(level 2)</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>toàn đối với</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>thẻ Token và</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Smart card</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>.2.3</p></blockquote></td>
<td><blockquote><p>Yêu cầu về
chính sách
và an toàn
cho các tổ
chức cung
cấp dịch vụ
tin cậy: Các
thành phần
dịch vụ vận
hành thiết bị
tạo chữ ký số
và hỗ trợ tạo
chữ ký số
AdES</p></blockquote></td>
<td><blockquote><p>Yêu cầu về</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ETSI TS
119 431-1</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Electronic Signatures</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Áp dụng cả bộ
tiêu chuẩn 2
phần;
Phiên bản V1.1.1
(12/2018)</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chính sách</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>and Infrastructures</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>và an toàn</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>(ESI); Policy and</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>cho các tổ</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>security requirements for</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chức cung</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>trust service providers;</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>cấp dịch vụ</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Part 1: TSP service</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>tin cậy: Các</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>components operating a</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>thành phần</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>remote QSCD/SCDev</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dịch vụ vận</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ETSI TS
119 431-2</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Electronic Signatures</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>hành thiết bị</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>tạo chữ ký số</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>and Infrastructures</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>và hỗ trợ tạo</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>(ESI); Policy and</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chữ ký số</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>security requirements for</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>AdES</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>trust service providers;</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Part 2: TSP service</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>components supporting</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>AdES digital signature</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>creation</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>.2.4</p></blockquote></td>
<td><blockquote><p>Giao thức
tạo chữ ký số
từ xa</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>ETSI TS
119 432</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Electronic Signatures</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Phiên bản V1.1.1
(03/2019)</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>and Infrastructures</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>(ESI); Protocols for</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>remote digital signature</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>creation</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>FIPS PUB</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>140-2</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Security Requirements</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>for Cryptographic</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>Modules</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>- Yêu cầu tối</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>thiểu mức 3</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>(level 3)</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>FIPS PUB</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>140-2</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Security Requirements</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>for Cryptographic</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>Modules</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>- Yêu cầu tối</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>thiểu mức 2</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>(level 2)</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>ETSI TS</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>119 431-1</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Áp dụng cả bộ</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>tiêu chuẩn 2</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>phần;</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>Phiên bản V1.1.1</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>(12/2018)</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>ETSI TS</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>119 431-2</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Giao thức</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>tạo chữ ký số</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>từ xa</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>ETSI TS</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>119 432</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Phiên bản V1.1.1</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>(03/2019)</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>.2.5</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Hệ thống tin</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>EN
419241-
1:2018</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Trustworthy Systems</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>cậy hỗ trợ ký</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Supporting Server</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>số từ xa -</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Signing - Part 1: General</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Các yêu cầu</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>system security</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chung</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>requirements</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>.2.6</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Hệ thống tin</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>EN
419241-
2:2019</p></blockquote></td>
<td><blockquote><p>Trustworthy Systems
Supporting Server
Signing - Part 2:
Protection Profile for
QSCD for Server Signing</p></blockquote></td>
<td><blockquote><p>Trustworthy Systems</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>cậy hỗ trợ ký</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Supporting Server</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>số từ xa –</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Signing - Part 2:</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Yêu cầu và</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Protection Profile for</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>mục tiêu (hồ</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>QSCD for Server Signing</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>sơ bảo vệ)</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>của thiết bị</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>tạo chữ ký số</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dành cho ký</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>số từ xa</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>.2.7</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Yêu cầu và</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>EN
419221-
5:2018</p></blockquote></td>
<td><blockquote><p>Protection Profiles for
TSP Cryptographic
modules - Part 5:
Cryptographic Module
for Trust Services</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>mục tiêu (hồ</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>sơ bảo vệ)</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>dành cho mô</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>đun bảo mật</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>phần cứng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>của tổ chức</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>cung cấp dịch</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>vụ tin cậy –</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>mô đun mã</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>hóa dành cho</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>các dịch vụ</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>tin cậy</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>33</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Tiêu chuẩn kiểm tra trạng thái chứng thư số</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>33.1</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Giao thức</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>RFC 2585</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Internet X.509 Public</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Áp dụng một</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>truyền, nhận</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Key Infrastructure -</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>hoặc cả hai giao</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>EN</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>419241-</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>1:2018</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>EN</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>419241-</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>2:2019</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>EN</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>419221-</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>5:2018</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Protection Profiles for</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>TSP Cryptographic</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>modules - Part 5:</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>Cryptographic Module</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>for Trust Services</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>chứng thư</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>Operational Protocols:
FTP and HTTP</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>thức FTP và
HTTP</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chữ ký số và</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>danh sách</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chứng thư</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chữ ký số bị</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>thu hồi</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>33.2</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Giao thức</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>RFC 8446</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>The Transport Layer</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Bắt buộc áp
dụng tối thiểu</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>bảo mật tầng</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Security (TLS) Protocol</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>giao vận</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Version 1.3</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>33.3</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Giao thức</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>RFC 2560</p></blockquote></td>
<td><blockquote><p>X.509 Internet Public
Key Infrastructure - On-
line Certificate status
protocol</p></blockquote></td>
<td><blockquote><p>X.509 Internet Public</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>cho kiểm tra</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>Key Infrastructure - On-</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>trạng thái</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>line Certificate status</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chứng thư</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>protocol</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>chữ ký sốtrực</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p>tuyến</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Operational Protocols:</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>FTP and HTTP</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>thức FTP và</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>HTTP</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Bắt buộc áp</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>dụng tối thiểu</p></blockquote></td>
</tr>
</tbody>
</table>


**Phụ lục II** 


**DANH MỤC TIÊU CHÍ ĐÁNH GIÁ HIỆU LỰC CỦA CHỨNG** 


**THƯ CHỮ KÝ SỐ VÀ CHỮ KÝ SỐ HỢP LỆ TRONG PHẦN MỀM KÝ** 


**SỐ, PHẦN MỀM KIỂM TRA CHỮ KÝ SỐ** 


*(Ban hành kèm theo Thông tư số /2025/TT-BKHCN ngày tháng năm 2025 của Bộ* 


*trưởng Bộ Khoa học và Công nghệ)* 



<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong>Số TT</strong></p></blockquote></th>
<th><blockquote><p><strong>Tiêu chí đánh giá</strong></p></blockquote></th>
<th><blockquote><p><strong>Hiệu lực/hợp lệ</strong></p></blockquote></th>
<th><blockquote><p><strong>Quy định áp dụng</strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>1</p></blockquote></td>
<td><blockquote><p>Tính hiệu lực của chứng thư chữ ký số</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>1.1</p></blockquote></td>
<td><blockquote><p>Thời gian có hiệu lực của chứng
thư số</p></blockquote></td>
<td><blockquote><p>Thời gian trên chứng
thư chữ ký số còn
hiệu lực tại thời
điểm ký số</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp dụng</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>1.2</p></blockquote></td>
<td><blockquote><p>Trạng thái chứng thư số qua danh
sách chứng thư chữ ký số thu hồi
(CRL) được công bố tại thời điểm
ký số hoặc bằng phương pháp
kiểm tra trạng thái chứng thư chữ
ký số trực tuyến (OCSP) ở chế độ
trực tuyến trong trường hợp tổ
chức cung cấp dịch vụ chứng thực
chữ ký số có cung cấp dịch vụ
OCSP</p></blockquote></td>
<td><blockquote><p>Trạng thái của
chứng thư chữ ký số
còn hoạt động tại
thời điểm ký số</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp dụng</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>1.3</p></blockquote></td>
<td><blockquote><p>Thuật toán mật mã trên chứng thư
chữ ký số</p></blockquote></td>
<td><blockquote><p>Các thuật toán mật
mã trên chứng thư
chữ ký số tuân thủ
theo quy định về quy
chuẩn, tiêu chuẩn kỹ
thuật bắt buộc áp
dụng về chữ ký số và
dịch vụ chứng thực</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp dụng</p></blockquote></td>
</tr>
</tbody>
</table>



<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
<th><blockquote><p><strong>chữ ký số đang có
hiệu lực</strong></p></blockquote></th>
<th><blockquote><p><strong></strong></p></blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote><p>1.4</p></blockquote></td>
<td><blockquote><p>Mục đích, phạm vi sử dụng của
chứng thư chữ ký số</p></blockquote></td>
<td><blockquote><p>Chứng thư chữ ký số
được sử dụng đúng
mục đích, phạm vi sử
dụng</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp dụng</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>1.5</p></blockquote></td>
<td><blockquote><p>Các tuyên bố khác của Tổ chức
cung cấp dịch vụ chứng thực chữ
ký số</p></blockquote></td>
<td><blockquote><p>Các tuyên bố khác
không nằm ngoài
phạm vi Quy chế
chứng thực của Tổ
chức cung cấp dịch
vụ chứng thực chữ
ký số</p></blockquote></td>
<td><blockquote><p>Khuyến nghị áp
dụng</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>2</p></blockquote></td>
<td><blockquote><p>Tính hợp lệ của chữ ký số</p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
<td><blockquote><p></p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>2.1</p></blockquote></td>
<td><blockquote><p>Thông tin về chủ thể ký</p></blockquote></td>
<td><blockquote><p>Kiểm tra, xác thực
được đúng thông tin
chủ thể ký số</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp dụng</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>2.2</p></blockquote></td>
<td><blockquote><p>Cách thức tạo chữ ký số</p></blockquote></td>
<td><blockquote><p>Chữ ký số được tạo
ra đúng bởi khóa bí
mật tương ứng với
khóa công khai trên
chứng thư chữ ký số</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp dụng</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>2.3</p></blockquote></td>
<td><blockquote><p>Chứng thư chữ ký số kèm theo
thông điệp dữ liệu</p></blockquote></td>
<td><blockquote><p>Chứng thư chữ ký số
có hiệu lực tại thời
điểm ký</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp dụng</p></blockquote></td>
</tr>
<tr>
<td><blockquote><p>2.4</p></blockquote></td>
<td><blockquote><p>Tính toàn vẹn của thông điệp dữ
liệu</p></blockquote></td>
<td><blockquote><p>Mã băm có được từ
việc băm thông điệp
dữ liệu và mã băm
có được khi giải mã
chữ ký số trùng nhau</p></blockquote></td>
<td><blockquote><p>Bắt buộc áp dụng</p></blockquote></td>
</tr>
</tbody>
</table>


**Phụ lục III** 


**HƯỚNG DẪN KẾT NỐI ĐẾN CỔNG KẾT NỐI DỊCH VỤ CHỨNG THỰC** 


**CHỮ KÝ SỐ CÔNG CỘNG** 


*(Ban hành kèm theo Thông tư số /2025/TT-BKHCN ngày tháng năm 2025 của Bộ* 


*trưởng Bộ Khoa học và Công nghệ)* 


# 1. Mô hình kết nối


Mô hình kết nối với Cổng kết nối dịch vụ chứng thực chữ ký số công cộng


(sau đây gọi là Cổng eSign) được mô tả tại sơ đồ như sau:


Chú thích:


- HTTT: Hệ thống thông tin phục vụ giao dịch điện tử sử dụng chữ ký số.


- CA: Tổ chức cung cấp dịch vụ chứng thực chữ ký số công cộng.


# 2. Các thông tin hướng dẫn kết nối


a) Giao thức sử dụng để kết nối là API, phương thức kết nối là POST.


b) Đường dẫn kết nối các API: https://esign.neac.gov.vn
c) Thông tin Cổng eSign cung cấp cho các HTTT gồm: sp_id và


sp_password hoặc token, trong đó:


- sp_id: Mã xác thực được cấp cho HTTT.


- sp_password: Mật khẩu kết nối được cấp cho HTTT tương ứng với sp_id.


- token: Thông tin xác thực được cấp cho HTTT.