import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTest(unittest.TestCase):
    def test_title_case_insensitive(self):
        lion = DigitalVideoDisc("The Lion King")
        discs = [lion, DigitalVideoDisc("Aladdin")]
        for keyword in ("lion", "LION", "LiOn", "The Lion King"):
            with self.subTest(keyword=keyword):
                self.assertEqual(search_by_title(discs, keyword), [lion])

    def test_title_search_boundaries(self):
        first = DigitalVideoDisc("The Lion King")
        second = DigitalVideoDisc("Lion Documentary")
        discs = [first, second, DigitalVideoDisc("Aladdin")]
        original = list(discs)
        self.assertEqual(search_by_title([], "lion"), [])
        self.assertEqual(search_by_title(discs, "missing"), [])
        self.assertEqual(search_by_title(discs, ""), discs)
        self.assertEqual(search_by_title(discs, "lion"), [first, second])
        self.assertEqual(discs, original)


if __name__ == "__main__":
    unittest.main()
