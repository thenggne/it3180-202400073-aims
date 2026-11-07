# Trả lời và báo cáo Lab 03

Sinh viên: Đinh Tiến Thành — MSSV 202400073. Làm một mình, mô phỏng Dev 2
bằng bản clone riêng; master vẫn yêu cầu PR với 0 approval.

## Merge base là gì?

Merge base là tổ tiên chung tốt nhất của hai commit: không có tổ tiên
chung khác mới hơn nó trong quan hệ tổ tiên. Git dùng nó làm mốc so sánh
ba chiều để kết hợp thay đổi của hai phía. Có thể có nhiều merge base
trong lịch sử phức tạp; git merge-base --all cho biết các mốc đó.

Trong bài, git merge-base 4ebf776 4b51d66 trả về 95b7cc5, mốc trước khi hai
nhánh cùng sửa thông báo thêm DVD. Hai thay đổi đụng cùng dòng nên merge
báo CONFLICT trong aims/cart.py.

## Vì sao master và release/* phải dùng revert?

Đây là lịch sử chung mà người khác hoặc bản nộp đang tham chiếu. Reset
hoặc rebase có thể dời nhánh, thay SHA và cần force push, gây mất đồng bộ.
Revert tạo commit đảo ngược mới, giữ lịch sử và lý do hoàn tác để kiểm
toán; bản hoàn tác vẫn đi qua nhánh riêng, kiểm thử và PR.

Với merge commit, -m 1 chọn parent 1 làm dòng chính cần giữ. Revert #14
loại phần khác biệt so với master trước merge, không xóa commit cũ.
Muốn đưa tính năng trở lại sau này cần thay đổi mới hoặc revert bản revert;
merge lại nguyên nhánh cũ thường không khôi phục phần đã hoàn tác.

## A — Bugfix từ master

- Issue #9: Cart accepts the 21st DVD although the limit is 20.
- c54c1f7 thêm regression test và kiểm tra tổng tiền. Chạy trước fix:
  test_add_dvd_until_full FAIL, AssertionError: True is not false.
- 97fe07e đổi > thành >= MAX_NUMBERS_ORDERED; 2 tests OK.
- PR #10 có Fixes #9, merge vào master; Issue #9 tự đóng.

## B — Bugfix từ feature

- feature/discount bắt đầu với công thức sai total * percent / 100.
- Dev 2 tạo bugfix/discount-calculation từ origin/feature/discount.
- 169d3eb thêm hai test: tổng sau giảm và từ chối phần trăm không hợp lệ.
  Chạy trước fix có lỗi tại 0, 20, 100, -1 và 150 phần trăm.
- 9ce476b tính total * (100 - percent) / 100, kiểm tra 0 <= percent <= 100.
- PR #11 có base feature/discount, chỉ sửa cart.py và test_cart.py.
  Sau đó PR #12 đưa tính năng đã sửa về master. 4 tests OK.

## C — Giải quyết xung đột bằng merge

- PR #13 đổi thông báo sang tiếng Việt; PR #14 thêm tiêu đề DVD.
- Hai nhánh tạo từ cùng mốc 95b7cc5. Merge #13 trước, Dev 2 fetch rồi
  merge origin/master: xuất hiện CONFLICT (content) tại aims/cart.py.
- Xóa dấu xung đột, kết hợp thành Đã thêm đĩa '<tên>' vào giỏ hàng.
- 864154e hoàn tất merge trên nhánh Dev 2; chạy 4 tests OK rồi push.
- PR #14 được merge vào master bằng merge commit 77b5ee4.
- Chọn cách merge trong hai cách của đề; không rebase nhánh đã chia sẻ.

## D — Reset, reflog và revert

Thực hành local trên topic/undo-practice, chỉ tạo .undo-practice.txt:

| Thao tác | Quan sát |
| --- | --- |
| reset --soft HEAD~1 | Bỏ commit, git status hiện A ở staging |
| reset --mixed HEAD~1 | Bỏ commit và staging; tệp mới hiện ?? |
| reset --hard HEAD~1 | Loại tệp nháp đã commit; working tree sạch |
| git reflog | Vẫn tìm thấy commit f3e1c45 đã bị bỏ khỏi đầu nhánh |

topic/undo-recovered giữ lại f3e1c45 để xem nội dung commit bị bỏ.
Cả hai nhánh thực hành không push. Không reset lịch sử master hoặc release.

PR #15 trên bugfix/revert-show-added-title dùng git revert -m 1 77b5ee4.
Commit đảo ngược 8b8a31a giữ thông báo tiếng Việt từ #13, bỏ phần thêm tên;
giới hạn 20 đĩa, discount và các test vẫn giữ nguyên. 4 tests OK sau revert.

## Kiểm tra cuối bài

- python -m unittest discover -s tests -v: 4 tests OK trên master.
- python main.py: Total cost: 63.89 $.
- Không còn dấu xung đột trong mã; Issue #9 Closed; có PR revert #15.
- release/lab03 được tạo từ master sau khi merge tài liệu này.
- Tìm kiếm phân biệt hoa thường được giữ nguyên cho bài hotfix Lab 05.
