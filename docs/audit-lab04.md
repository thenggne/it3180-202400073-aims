# Kiểm toán cấu hình Lab 04

Sinh viên: Đinh Tiến Thành — MSSV 202400073. Ngày: 2026-11-07.

## Baseline và tag

| Annotated tag | Commit đích | Nhánh bản nộp |
| --- | --- | --- |
| v0.1.0 | 5f46d45 | release/lab01 |
| v0.2.0 | 40b52aa | release/lab02 |
| v0.3.0 | a4788bf | release/lab03 |
| v1.0.0 | 1e11df5 | release/lab04 |

git cat-file -t trả về tag cho cả bốn tag, không phải lightweight tag.
v1.0.0 được tạo sau merge PR #17; trùng đầu origin/release/lab04.
Tag đã push không bị đổi hoặc xóa.

## Bảo vệ release

Ruleset Protect release branches (ID 26760528) đang active, áp dụng
refs/heads/release/*, không có bypass actor; chặn xóa và non-fast-forward,
bắt buộc PR và giải quyết review thread. Required approvals là 0 vì làm
một mình; dismiss stale reviews bật.

Đã tạo commit rỗng ac18e29 trên topic/release-protection-check (chỉ local,
không có PR) và thử push HEAD:release/lab04. GitHub từ chối với GH013:
Changes must be made through a pull request. Baseline không thay đổi.

## GitHub Release và đóng gói

[AIMS-mini 1.0.0](https://github.com/thenggne/it3180-202400073-aims/releases/tag/v1.0.0)
được publish, không phải draft/prerelease; target release/lab04, tag có sẵn
v1.0.0. Release notes gồm mục 1.0.0 từ CHANGELOG và ghi chú GitHub tạo.

Đã chạy git archive từ v1.0.0, prefix aims-1.0.0/, tạo dist/aims-1.0.0.zip
và đính kèm Release. ZIP có 21 mục, không có __pycache__ hoặc .pyc.

SHA-256: 987763e9344ceb94673bfb8d47e42f175aef76c541919a98cb8f83a59ba96955.

## Tái tạo và kiểm thử phiên bản cũ

- Detached HEAD tại v0.2.0: python -B -X utf8 main.py in tổng 63.89 USD;
  sau đó quay lại master.
- Worktree riêng tại v1.0.0: xác nhận import aims từ đúng thư mục worktree,
  __version__ là 1.0.0; python -B -m unittest discover -s tests -v: 4 tests OK.
- Demo trong worktree in AIMS-mini v1.0.0 và Total cost: 63.89 $.
- git show v1.0.0:aims/__init__.py trả về __version__ = "1.0.0".
- git ls-tree tại tag không có tệp nháp, clone Dev 2, worktree hay sản phẩm
  build. Worktree kiểm toán đã được gỡ bằng git worktree remove.
- Giữ lệnh -X utf8 để terminal Windows dùng mã hóa cũ in được tiếng Việt.

## Phát triển sau phát hành và status accounting

PR #18 thêm sort_by_title, sort_by_cost và hai test vào master; CHANGELOG
ghi ở Unreleased. Sáu test đạt, gồm giỏ trống/một đĩa, thứ tự, giữ thứ tự
khi khóa bằng nhau và không đổi tổng tiền. Demo vẫn tổng 63.89 USD.
Hai phương thức không có tại v1.0.0 hoặc release/lab04.

Kết quả ngay sau merge PR #18 (trước PR báo cáo này):

```text
git log --oneline release/lab04..master
189615a Merge pull request #18 from thenggne/feature/sort-cart
4b61117 feat: add sort_by_title and sort_by_cost to Cart

git log --oneline master..release/lab04
(rỗng)

git describe --tags
v1.0.0-2-g189615a
```

git diff --stat v0.3.0 v1.0.0: 4 tệp, 107 dòng thêm (version, banner,
CHANGELOG và câu trả lời). git diff --stat v1.0.0 master tại mốc trên:
3 tệp, 59 dòng thêm (sắp xếp, test, Unreleased).

Sau khi báo cáo được merge, master tiến thêm commit tài liệu; đó là kết
quả đúng của A..B và git describe. Không đưa thay đổi mới về release/lab04,
không tạo release/lab05 trước bài tiếp theo.
