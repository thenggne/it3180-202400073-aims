# Trả lời thảo luận Lab 04

Sinh viên: Đinh Tiến Thành — MSSV 202400073. Làm một mình.

## Vì sao chuẩn bị phát hành trên master trước?

Chuẩn bị version, CHANGELOG và demo trên nhánh topic rồi PR vào master
giúp kiểm thử một trạng thái tích hợp thống nhất. Sau đó tạo release từ
chính trạng thái đó. Nếu sửa trực tiếp trên release, master có thể thiếu
cấu hình phát hành và các dòng phát triển dễ lệch nhau.

## Vì sao release/* không merge ngược vào master?

Trong Release Flow của học phần, release là dòng bảo trì/bản nộp và có
cấu hình phiên bản riêng. Merge toàn bộ về master có thể kéo số phiên bản
cũ hoặc thay đổi chỉ dành cho bản đã phát hành. Bản sửa cần thiết được
đưa về các dòng bị ảnh hưởng qua nhánh và PR, thường cherry-pick -x commit
sửa lỗi để truy vết; không đưa cả commit nâng phiên bản riêng của release.

## So sánh với GitFlow

GitFlow có develop để tích hợp tính năng và main để lưu bản phát hành;
nhánh release thường tách từ develop, hoàn tất rồi merge về main và
develop. Hotfix thường xuất phát từ main rồi đồng bộ về develop.
Release Flow trong bài tích hợp tính năng trực tiếp vào master qua PR,
tạo release/labXX từ master và giữ nhiều dòng bảo trì. Không có develop,
không merge release ngược về master.

## Vì sao lên 1.0.0 thay vì 0.4.0?

Các bản 0.y.z là giai đoạn phát triển ban đầu. Trong bài, Lab 04 chọn mốc
1.0.0 để công bố baseline/API ổn định và bắt đầu cam kết tương thích.
Đó là quyết định phát hành của dự án, không phải vì lab thứ tư bắt buộc
lên major. Nếu dự án chưa sẵn sàng ổn định thì 0.4.0 vẫn là lựa chọn hợp lý.
Sau 1.0.0: sửa lỗi tương thích tăng PATCH, thêm tính năng tương thích tăng
MINOR, thay đổi không tương thích tăng MAJOR.

## Tag khác nhánh release thế nào?

Annotated tag là đối tượng có thông điệp, tác giả và thời điểm, định danh
một commit cụ thể; tag đã chia sẻ không được di chuyển hay xóa. Nhánh
release có thể tiến thêm khi nhận hotfix qua PR. Ban đầu v1.0.0 trùng
đầu release/lab04; tag vẫn cố định sau khi nhánh nhận bản vá.

## Quy tắc bài cá nhân và kiểm toán

release/* yêu cầu PR, không có quyền bypass, chặn force push và xóa nhánh.
Số approval bắt buộc là 0 cho bài cá nhân, vì tác giả không tự approve được;
đây là điều chỉnh từ cấu hình 1 approval minh họa ở trang 48, nhất quán
với chế độ làm một mình ở trang 29.

A..B liệt kê commit có trong B nhưng không có trong A. Dùng log và diff
để biết master đi trước baseline những gì. Tái tạo bản cũ bằng detached
HEAD hoặc worktree, chạy test và kiểm tra version/CHANGELOG/tệp được theo
dõi tại đúng tag. git archive chỉ đóng gói tệp được theo dõi tại tag đó.
