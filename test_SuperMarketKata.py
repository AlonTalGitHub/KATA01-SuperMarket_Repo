# ----------------------------------------------- #
# Intro to Kata 01:                               #
# Super_Market management & pricing kata Project. #
# ----------------------------------------------- #
# Background
# ==========
# Writing a program witch operates
# the supermarket.
#
# Project Description
# ====================
# In this super market we have entities witch are mainly objects:
# The super market's objects are:
#
# Inventory Managment - handle the stock:
#   1) the inventory is a list or a dictionary of products (the key) and how many in stock (value).
#   2) add and remove products or a few units from its stock from the warehouse.
#   3) prints the full stock.
#
# A Product - entity:
#   Every Product contains the fields:
#     1) Barcode.
#     2) Category.
#     3) Name.
#     4) Full Price.
#     5) Units of measuring.
#
# A Shopping Cart - entity:
#   Every Cart Is:
#     1) A list or a dictionary of products (the key) and how many of each one in the cart (value).
#     2) add and remove products or a few units from the cart.
#
# -----------------------------------------------------------------------------
#
# Example string input. Use it to test your code.
#
# my_product = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 'small packs')
# my_inventory = InventoryMgmt()
# my_inventory.add_to_stock(my_product, 200)
# my_cart = ShoppingCart()
# my_cart.add_product(my_product, 7)
# my_inventory.remove_from_stock(my_product, 7)
# print my_inventory
# print my_cart
# print my_product

import unittest
from SuperMarketKata import ShoppingCart
from SuperMarketKata import Product


class TestShoppingCart(unittest.TestCase):

    def test_add_product(self):
        my_product = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 'small packs')
        my_cart_1 = ShoppingCart()

        self.assertEqual(str(my_cart_1.add_product(my_product, 20)),
                         '{Product(73459, Milk & Eggs, yammy eggs, 12.5, small packs): 20}')

if __name__ == '__main__':
    unittest.main()