# Trả lời thảo luận Lab 05

Sinh viên: Đinh Tiến Thành — MSSV 202400073. Làm một mình.

## Upstream first so với release first

Upstream first sửa trên dòng phát triển chính rồi backport về bản phát
hành. Ưu điểm: bản sửa luôn có trên phiên bản tương lai, giảm nguy cơ quên
master, kiểm thử cùng mã mới. Nhược điểm: master có thể khác xa bản đang
lỗi; bản vá có phụ thuộc mới và khó áp dụng về phiên bản cũ.

Release first như bài học sửa từ đúng release đang bị lỗi, kiểm thử và
phát hành bản vá nhỏ cho người dùng sớm. Nhược điểm: phải chủ động đưa
bản sửa lên master và mọi release còn bị ảnh hưởng; quên một dòng sẽ để
lỗi tái xuất hiện. Chọn mô hình theo độ lệch mã nguồn và nhu cầu bảo trì.

## Nếu quên đưa bản sửa sang release/lab05 thì phát hiện bằng lệnh nào?

Lệnh kiểm tra hành vi ở phần F chạy trên v1.0.1, v1.1.0 và master:
tìm 'lion' phải trả về đúng một DVD ở cả ba. Nếu release/lab05 chưa sửa,
v1.1.0 sẽ trả về 0 thay vì 1. Trước khi gắn tag, kiểm tra trực tiếp
origin/release/lab05 cũng phát hiện được.

git log --all --grep='cherry picked from commit <FIX_SHA>' kỳ vọng có
hai commit sao chép, một ở master và một ở release/lab05. Cần kiểm tra
commit nào thuộc nhánh nào, không chỉ đếm kết quả toàn repo.
git cherry -v origin/release/lab05 origin/release/lab04 cho thấy bản sửa
ở release/lab04 là '+' nếu chưa có patch tương đương bên lab05, '-' nếu có.
git tag --contains chỉ kiểm tra quan hệ tổ tiên, không nhận diện patch
tương đương được cherry-pick với SHA khác.

## Vì sao tách commit sửa lỗi và commit nâng phiên bản?

Chỉ cherry-pick commit mã và regression test với -x để ghi nguồn gốc.
Không đưa commit 1.0.1 lên dòng 1.1.0 vì sẽ ghi đè số phiên bản và xung
đột cấu hình. Cập nhật CHANGELOG của mỗi dòng bằng commit riêng.

## Vì sao chưa gắn v1.1.0 khi vừa tạo release/lab05?

Trong bài, bản này còn phải nhận hotfix trước khi công bố. Tag phát hành
đã chia sẻ phải giữ cố định; nếu đã công bố v1.1.0 rồi mới sửa lỗi, cần
phát hành bản vá v1.1.1, không di chuyển tag v1.1.0.

## CI và kiểm soát thay đổi

Workflow test chạy trên pull_request vào master/release/** và push master.
Chỉ bắt buộc status check sau khi đã có workflow chạy và biết đúng tên
check. Bài cá nhân yêu cầu PR với 0 approval, không bypass. Bài thử CI
cố ý phá total_cost chỉ nằm trên nhánh PR riêng; không merge mã lỗi vào
master và không tắt bảo vệ để vượt qua check thất bại.
