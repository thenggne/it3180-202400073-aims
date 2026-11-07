import contextlib
import io
import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class CartTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.output = contextlib.redirect_stdout(io.StringIO())
        self.output.__enter__()
        self.addCleanup(self.output.__exit__, None, None, None)

    def test_add_dvd_until_full(self):
        for index in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(self.cart.add_dvd(DigitalVideoDisc(str(index))))
        self.assertFalse(self.cart.add_dvd(DigitalVideoDisc("The 21st DVD")))
        self.assertEqual(len(self.cart.items), MAX_NUMBERS_ORDERED)

    def test_total_cost(self):
        for cost in (19.95, 24.95, 18.99):
            self.cart.add_dvd(DigitalVideoDisc("DVD", cost=cost))
        self.assertAlmostEqual(self.cart.total_cost(), 63.89)

    def test_discounted_total(self):
        self.cart.add_dvd(DigitalVideoDisc("DVD", cost=100))
        for percent, expected in ((0, 100), (20, 80), (100, 0)):
            with self.subTest(percent=percent):
                self.assertAlmostEqual(
                    self.cart.total_cost_with_discount(percent), expected)

    def test_invalid_discount(self):
        for percent in (-1, 150):
            with self.subTest(percent=percent):
                with self.assertRaises(ValueError):
                    self.cart.total_cost_with_discount(percent)


if __name__ == "__main__":
    unittest.main()
