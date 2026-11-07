# Trả lời thảo luận Lab 01

Sinh viên: Đinh Tiến Thành — MSSV 202400073

## Vì sao dùng git mv?

`git mv` chuyển hoặc đổi tên tệp và đưa thay đổi vào staging trong một lệnh,
giúp tránh quên stage việc xóa đường dẫn cũ. Git vẫn nhận diện đổi tên dựa
trên độ giống nhau của nội dung, kể cả khi dùng mv rồi git add.
`git log --follow -- aims/cart.py` cho phép xem tiếp lịch sử trước khi đổi tên.

## release/lab01 có phải baseline không?

Có. Nhánh này xác định phiên bản đã thống nhất để nộp và kiểm toán Lab 01.
Khi tạo, nó trỏ cùng commit với master. Nhánh có thể di chuyển nên cần giữ
quy trình kiểm soát thay đổi; annotated tag sẽ xác định chính xác một bản
phát hành ở các lab sau. Không merge release ngược vào master.

## Vì sao không commit thẳng master dù làm một mình?

Nhánh riêng và Pull Request giúp tách thay đổi đang làm khỏi phiên bản ổn
định, xem diff, ghi mục đích và cách kiểm thử trước khi tích hợp. Lịch sử PR
cho phép truy vết và tạo thói quen làm việc nhóm. Phần khởi tạo A–C trong
Lab 01 hướng dẫn commit trực tiếp; từ refactor flow, thay đổi đi qua PR.

## Cấu hình global khác local thế nào?

`git config --global` thường lưu trong ~/.gitconfig (hoặc vị trí XDG), áp dụng
cho các repo của người dùng. `--local` lưu trong .git/config của repo hiện tại
và ưu tiên hơn global cho cùng khóa. Dùng git config --list --show-origin
để xem nguồn cấu hình thực tế.
