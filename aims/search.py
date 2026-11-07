def search_by_category(items, keyword):
    """Tìm DVD có thể loại chứa từ khóa, không phân biệt hoa thường."""
    return [dvd for dvd in items if keyword.lower() in dvd.category.lower()]


def search_by_title(items, keyword):
    """Tìm DVD có tiêu đề chứa keyword, phân biệt hoa thường."""
    return [dvd for dvd in items if keyword in dvd.title]
