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
# Inventory Management - handle the stock. meaning, only add and remove products from the warehouse.
# For this super market we would need a few objects:
#
# Project Description
# ====================
# In this super market we have entities witch are mainly objects:
# The super market's objects are:
#
# Inventory Management - handle the stock:
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
#     5) Sale Price.
#     6) Units of measuring the quantity.
#
# A Cart - entity:
#   Every Cart Is:
#     1) A list or a dictionary of products (the key) and how many of each one in the cart (value).
#     2) add and remove products or a few units from the cart.
#
# -----------------------------------------------------------------------------


class Product(object):
    def __init__(self, barcode, category, name, full_price, sale_price, units):
        self.barcode = barcode
        self.category = category
        self.name = name
        self.full_price = full_price
        self.sale_price = sale_price
        self.units = units

    def __repr__(self):
        return '{self.__class__.__name__}({self.barcode}, {self.category},' \
               ' {self.name}, {self.full_price}, {self.sale_price}, {self.units})'.format(self=self)


class Inventory(object):

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

        if self.stock[product] < quantity:
            print 'you tried to remove %d more %s than in the Inventry.' \
                  ' you removed all.' % (quantity - self.stock[product],
                                         product.name)
            self.stock[product] = 0
            print ('This product is no longer in Inventory.')

    def __repr__(self):
        return '{self.__class__.__name__}({self.stock})'.format(self=self)


class Cart(object):

    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):

        if product not in self.products:
            self.products[product] = quantity
            return self.products
        else:
            self.products[product] += quantity

    def remove_product(self, product, quantity):

        if product not in self.products:
            print 'This product is not in the cart.'

        if product in self.products and self.products[product] >= quantity:
            self.products[product] -= quantity

        if self.products[product] < quantity:
            print 'you tried to remove %d more %s than in cart.' \
                  ' you removed all.' % (quantity - self.products[product],
                                         product.name)
            self.products[product] = 0
            print ('This product is no longer in cart.')
        if quantity == 'all':
            self.products[product] = 0
            print 'This product is no longer in cart, you removed all.'

    def __repr__(self):
        return '{self.__class__.__name__}({self.products})'.format(self=self)