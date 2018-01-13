# ----------------------------------------------- #
# Intro to Kata 01:                               #
# Super_Market management & pricing kata Project. #
# ----------------------------------------------- #
#
# Background
# ==========
# Writing a program witch operates
# the supermarket.
#
# In this super market we have:
#
# Inventory Managment - handle the stock. meaning, only add and remove products from the warehouse.
# For this super market we would need a few objects:
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
# Examples. Use it to test your code.
# inventory_Mgmt = {'Milk & Eggs': ['eggs', 'milk'], 'Fruits & Vegetables': ['banana', 'tomato'],
#                   'Meet, Chicken and Fish': ['chest', 'ham'], 'Bread & Bakery': ['rye bread', 'tortilla'],
#                   'Frozen & Salads': ['tivol', 'sandfrost']}
# -----------------------------------------------------------------------------


class Product(object):
    def __init__(self, barcode, category, name, full_price, units):
        self.barcode = barcode
        self.category = category
        self.name = name
        self.full_price = full_price
        self.units = units

    def __repr__(self):
        return '{self.__class__.__name__}({self.barcode}, {self.category},' \
               ' {self.name}, {self.full_price}, {self.units})'.format(self=self)


class InventoryMgmt(object):

    def __init__(self):
        self.stock = {}

    def add_to_stock(self, product, quantity):

        if product not in self.stock:
            self.stock[product] = quantity
        else:
            self.stock[product] += quantity

    def remove_from_stock(self, product, quantity):

        if product in self.stock and self.stock[product] >= quantity:
            self.stock[product] -= quantity
        else:
            print ('This product is not in stock.')

    def __repr__(self):
        return '{self.__class__.__name__}({self.stock})'.format(self=self)


class ShoppingCart(object):

    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):

        if product not in self.products:
            self.products[product] = quantity
            return self.products
        else:
            self.products[product] += quantity

    def remove_product(self, product, quantity):

        if product in self.products and self.products[product] >= quantity:
            self.products[product] -= quantity

        if self.products[product] < quantity:
            print 'you tried to remove %d more %s than in cart. you removed all.' % (quantity - self.products[product],
                                                                                     product.name)
            self.products[product] = 0
            print ('This product is no longer in cart')

    def __repr__(self):
        return '{self.__class__.__name__}({self.products})'.format(self=self)