import unittest
from supermarket.super_market import Product
from supermarket.sale import PercentOffSale


class TestPercentOffSale(unittest.TestCase):

    def test_(self):
        product = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 'small packs')
        sale_product = PercentOffSale(product, 0.5)
        self.assertEqual(sale_product.percent_price, 6.25)


if __name__ == '__main__':
    unittest.main()