# Changelog

Các thay đổi đáng chú ý của AIMS-mini được ghi theo Keep a Changelog.
Số phiên bản theo Semantic Versioning.

## [Unreleased]

## [1.1.0] - 2026-11-07

### Added

- search_by_category() tìm chuỗi con trong thể loại, không phân biệt hoa thường.
- Cart.sort_by_title() và Cart.sort_by_cost() sắp xếp giỏ tại chỗ tăng dần,
  giữ thứ tự tương đối khi khóa bằng nhau; không đổi tổng tiền.
- Kiểm thử sắp xếp theo tiêu đề và giá, gồm giỏ trống và một đĩa.

## [1.0.0] - 2026-11-07

### Added

- Package aims gồm DigitalVideoDisc và Cart; chương trình demo tổng 63.89 USD.
- Cart.print_cart() hiển thị chi tiết giỏ và xử lý giỏ trống.
- search_by_title() tìm chuỗi con trong tiêu đề, phân biệt hoa thường.
- Cart.total_cost_with_discount() trả tổng tiền sau giảm từ 0 đến 100%.
- Bốn regression tests cho giới hạn giỏ, tổng tiền và giảm giá.
- PR template, sơ đồ use case và câu trả lời Lab 01–04.
- __version__ và thông báo AIMS-mini v1.0.0 khi chạy demo.

### Fixed

- Từ chối DVD thứ 21 khi giỏ đã có 20 đĩa (Issue #9, PR #10).
- Sửa công thức giảm giá và từ chối phần trăm ngoài khoảng 0–100 (PR #11).

### Changed

- Thông báo thêm đĩa dùng tiếng Việt; phần tên DVD đã được hoàn tác bằng PR #15.

## [0.3.0] - 2026-11-07

### Added

- Luồng sửa lỗi có test tái hiện, xử lý xung đột và thực hành hoàn tác Lab 03.

### Fixed

- Giới hạn 20 DVD và công thức giảm giá.

## [0.2.0] - 2026-11-07

### Added

- In giỏ, tìm theo tiêu đề, PR template và use case của Lab 02.

## [0.1.0] - 2026-11-07

### Added

- Mã DVD, giỏ hàng, demo và cấu trúc package ban đầu của Lab 01.
