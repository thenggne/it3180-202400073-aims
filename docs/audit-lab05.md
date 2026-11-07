# Kiểm toán hotfix và CI — Lab 05

Sinh viên: Đinh Tiến Thành — MSSV 202400073. Ngày: 2026-11-07.

## Chuẩn bị dòng 1.1.0

- PR #20 thêm search_by_category phía trên search_by_title, không đổi phần
  ngữ cảnh hotfix tiêu đề. Đã kiểm tra hoa/thường, không khớp và danh sách trống.
- PR #21 chuẩn bị version 1.1.0, CHANGELOG và answers-lab05.md.
- Tạo release/lab05 từ master nhưng chưa gắn tag, để nhận bản sửa trước
  khi công bố. Các quy tắc bảo vệ release/* tiếp tục áp dụng.

## Tái hiện và sửa lỗi

Worktree tách biệt tại v1.0.0 trả [] khi tìm 'lion' trong The Lion King.
Issue #22 ghi tác động tới release/lab04, release/lab05 và master.
Regression tests mới thất bại trước fix với lion/LION/LiOn và nhiều kết quả.

Nhánh hotfix/search-case-insensitive tạo từ origin/release/lab04,
không có sorting hoặc category search mới của master.

- Commit sửa mã/test: 8faed65fa980152d34dc56d2be86b27a7945e394, Refs #22.
- Commit nâng riêng dòng 1.0.x: b39e4fb, version 1.0.1 và CHANGELOG.
- PR #23 vào release/lab04 chỉ có search.py, test_search.py, __init__.py,
  CHANGELOG.md; sau merge gắn annotated tag v1.0.1 tại a67386f.
- v1.0.0 giữ nguyên 1e11df5; diff v1.0.0..v1.0.1 đúng bốn tệp.
- Issue còn Open sau merge vào release; tự đóng sau merge PR #24 vào master.

## Lan truyền có truy vết

| Dòng | Bản sao commit fix | PR | Version |
| --- | --- | --- | --- |
| release/lab04 | 8faed65 (gốc) | #23 | 1.0.1 |
| master | cd9b5ef | #24 | 1.1.0 |
| release/lab05 | 03f44f3 | #25 | 1.1.0 |

Hai bản sao dùng cherry-pick -x, có trailer
(cherry picked from commit 8faed65fa980152d34dc56d2be86b27a7945e394).
Không cherry-pick commit version 1.0.1 sang dòng 1.1.0. CHANGELOG mỗi dòng
được cập nhật bằng commit riêng. Không xóa/tạo lại release hoặc merge toàn
bộ nhánh hotfix cũ vào master.

```text
git log --all --oneline --grep 'cherry picked from commit 8faed65fa980152d34dc56d2be86b27a7945e394'
03f44f3 fix: make search_by_title case-insensitive
cd9b5ef fix: make search_by_title case-insensitive

git tag --contains 8faed65fa980152d34dc56d2be86b27a7945e394
v1.0.1

git cherry -v origin/master origin/release/lab04
- 8faed65fa980152d34dc56d2be86b27a7945e394 fix: make search_by_title case-insensitive
+ b39e4fbf6d505b69952aa987d4c330173eae42e6 chore: bump version to 1.0.1
```

Dấu '-' xác nhận patch tương đương đã có trên master; '+' cho version
bump là đúng chủ đích. Tag --contains không nhận diện các bản cherry-pick
với SHA khác. Kiểm tra hành vi tìm 'lion' trên ba dòng đều phải ra 1.

## CI mở rộng và phép thử chặn merge

- PR #26 thêm workflow CI trên master; PR #27 đưa cùng workflow vào
  release/lab05 trước tag. Python 3.12, job test, quyền contents: read,
  chạy pull_request tới master/release/** và push master.
- CI của #26 và #27 đều pass. master yêu cầu status test (GitHub Actions),
  strict=true, áp dụng cho quản trị viên, 0 approval cho bài cá nhân.
- PR #28 cố ý cộng thêm 1 vào total_cost; CI test FAILURE và PR có trạng
  thái mergeStateStatus=BLOCKED. Đã đóng PR, không merge; xóa nhánh remote.
- Run lỗi để đối chiếu:
  https://github.com/thenggne/it3180-202400073-aims/actions/runs/42385078263
- Workflow không được thêm ngược vào v1.0.1: bản vá 1.0.x giữ đúng bốn
  tệp thay đổi. Các release cũ chưa có workflow cần bổ sung riêng nếu muốn
  tự chạy CI trên PR tạo hoàn toàn từ chính các nhánh cũ đó.

## Chốt bản nộp và kiểm tra

Sau merge báo cáo này vào release/lab05, gắn annotated tag v1.1.0 từ đúng
nhánh này; không di chuyển các tag đã chia sẻ. Báo cáo và CHANGELOG cũng
được đưa về master qua nhánh/PR riêng, không merge release vào master.

| Phiên bản | Số test kỳ vọng | Tìm lion | Version |
| --- | --- | --- | --- |
| v1.0.1 | 6 | 1 DVD | 1.0.1 |
| v1.1.0 | 8 | 1 DVD | 1.1.0 |
| master | 8 | 1 DVD | 1.1.0 |

Chạy unittest và kiểm tra hành vi tại từng ref sau khi gắn tag. Demo dùng
python -X utf8 main.py trên terminal Windows, tổng vẫn 63.89 USD.
Bản vá 1.0.1 không có sorting/category; bản 1.1.0 có cả hai.
