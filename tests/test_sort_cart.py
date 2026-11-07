import contextlib
import io
import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartSortTest(unittest.TestCase):
    def make_cart(self, discs):
        cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()):
            for disc in discs:
                cart.add_dvd(disc)
        return cart

    def test_sort_by_title(self):
        discs = [DigitalVideoDisc("Zebra", cost=30),
                 DigitalVideoDisc("Aladdin", cost=20),
                 DigitalVideoDisc("Aladdin", cost=10)]
        for items, expected in (([], []), ([discs[0]], [discs[0]]),
                                (discs, [discs[1], discs[2], discs[0]])):
            with self.subTest(size=len(items)):
                cart = self.make_cart(items)
                original_total = cart.total_cost()
                cart.sort_by_title()
                self.assertEqual(cart.items, expected)
                self.assertEqual(cart.total_cost(), original_total)

    def test_sort_by_cost(self):
        discs = [DigitalVideoDisc("Star Wars", cost=30),
                 DigitalVideoDisc("The Lion King", cost=10),
                 DigitalVideoDisc("Aladdin", cost=10)]
        for items, expected in (([], []), ([discs[0]], [discs[0]]),
                                (discs, [discs[1], discs[2], discs[0]])):
            with self.subTest(size=len(items)):
                cart = self.make_cart(items)
                original_total = cart.total_cost()
                cart.sort_by_cost()
                self.assertEqual(cart.items, expected)
                self.assertEqual(cart.total_cost(), original_total)


if __name__ == "__main__":
    unittest.main()
