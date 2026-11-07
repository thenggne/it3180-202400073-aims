# Trả lời và báo cáo Lab 02

Sinh viên: Đinh Tiến Thành — MSSV 202400073. Hình thức: làm một mình.

## Vì sao phải đồng bộ master trước khi PR?

Nhánh tính năng có thể được tạo từ master cũ. Fetch rồi merge origin/master
giúp kiểm tra tính năng với mã mới, xử lý xung đột sớm và chạy lại chương
trình trước khi tích hợp. Không có xung đột văn bản chưa có nghĩa là không
có lỗi tích hợp. PR vẫn phải được kiểm tra lại nếu master tiếp tục thay đổi.

Dev 2 tạo feature/search-by-title trước khi cart-print được merge. Sau đó
đã fetch và merge origin/master, chạy demo có print_cart trước khi tạo PR #6.

## Khi nào không được rebase?

Không rebase master, release hoặc lịch sử đã chia sẻ mà người khác đang
dựa vào: rebase thay SHA, có thể buộc người khác sửa lại lịch sử của họ.
Trong bài, chỉ viết lại commit chưa chia sẻ hoặc nhánh riêng được phép.
Rebase and merge của GitHub tạo commit mới trên nhánh đích, không force
push để viết lại các commit cũ đã có trên master.

## feature/* khác topic/* ra sao?

feature/* dành cho tính năng như in giỏ hoặc tìm kiếm. topic/* dành cho một
chủ đề thay đổi như tài liệu hoặc PR template. Cả hai là nhánh ngắn hạn,
tạo từ master và tích hợp về master qua PR; tên nhánh thể hiện mục đích.

## So sánh ba kiểu merge

| Kiểu | Commit chi tiết | Lịch sử | Hoàn tác tính năng |
| --- | --- | --- | --- |
| Merge commit | Giữ nguyên SHA | Có nhánh và commit merge | Revert commit merge với -m 1 |
| Squash | Gộp thành một commit mới | Tuyến tính ở điểm tích hợp | Revert commit đã gộp |
| Rebase | Giữ nội dung từng commit, SHA mới | Tuyến tính ở điểm tích hợp | Có thể cần revert nhiều commit |

PR #5 cart-print dùng merge commit, PR #6 search dùng squash,
PR #7 use-case dùng rebase. git log --oneline --graph thể hiện ba kết quả.

## Kiểm tra và giới hạn bài cá nhân

- master yêu cầu PR, áp dụng cả quản trị viên; 0 approval theo lựa chọn
  làm một mình trong đề; dismiss stale reviews bật; không force push/xóa.
- Commit nháp không có PR bị từ chối với GH006:
  Changes must be made through a pull request. Commit nháp chỉ ở máy.
- Push đúng đầu nhánh PR template đang mở đã được GitHub chấp nhận và
  PR #4 được đánh dấu merged; không coi trường hợp này là phép thử bị chặn.
- PR #5 được tạo với hai commit, sau đó bổ sung commit xử lý giỏ trống.
  Đã kiểm tra giỏ trống in The cart is empty và demo tổng 63.89 USD.
- GitHub không cho tác giả tự Request changes hoặc Approve PR của mình.
  Vì làm một mình, không có chuỗi review Changes requested → Approved;
  không mô phỏng danh tính reviewer. Đây là mục checklist chưa thể đạt
  nguyên văn khi không có tài khoản reviewer độc lập.
- Không sửa lỗi nhận đĩa thứ 21 (Lab 03) hoặc tìm phân biệt hoa thường
  (Lab 05) trong Lab 02.
