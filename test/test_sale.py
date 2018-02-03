import unittest
from supermarket.super_market import Product, Cart
from supermarket.sale import XPercent, OnePlusOne


class TestXPercent(unittest.TestCase):

    def test_apply(self):
        product1 = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 12.50, 'small packs')
        product2 = Product(43568, 'Meet & Chicken', 'shnitzel', 43.50, 43.50, 'kg')
        product3 = Product(76768, 'Drinks & Alkohol', 'wain', 55.50, 55.50, 'bottles')

        cart = Cart()
        cart.add_product(product1, 2)
        cart.add_product(product2, 3)
        cart.add_product(product3, 6)

        sale1 = XPercent(product1, 30)

        assert sale1.apply(cart) == 7.5


class TestOnePlusOne(unittest.TestCase):

    def test_apply(self):
        product1 = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 12.50, 'small packs')
        product2 = Product(43568, 'Meet & Chicken', 'shnitzel', 43.50, 43.50, 'kg')
        product3 = Product(76768, 'Drinks & Alkohol', 'wain', 55.50, 55.50, 'bottles')

        cart = Cart()
        cart.add_product(product1, 2)
        cart.add_product(product2, 1)
        cart.add_product(product3, 6)

        pay_for_products = OnePlusOne(product1, product3)
        pay_for_products2 = OnePlusOne(product1, product2)

        self.assertEqual(pay_for_products.apply(cart), 111)
        self.assertEqual(pay_for_products2.apply(cart), 25.0)
        self.assertEqual(cart.products[product1], 2)
        self.assertEqual(cart.products[product2], 2)


class TestXforFix(unittest.TestCase):

    def test_apply(self):
        product1 = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 12.50, 'small packs')
        product2 = Product(43568, 'Meet & Chicken', 'shnitzel', 43.50, 43.50, 'kg')
        product3 = Product(76768, 'Drinks & Alkohol', 'wain', 55.50, 55.50, 'bottles')

        cart = Cart()
        cart.add_product(product1, 2)
        cart.add_product(product2, 1)
        cart.add_product(product3, 6)


if __name__ == '__main__':
    unittest.main() 