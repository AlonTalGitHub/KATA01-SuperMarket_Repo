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

# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged
# to define any additional helper procedures that can assist you in accomplishing
# a task. You are encouraged to test your code by using print statements and the
# Test Run button.
# -----------------------------------------------------------------------------
# Example string input. Use it to test your code.
# inventory_Mgmt = {'Milk & Eggs': ['eggs', 'milk'], 'Fruits & Vegetables': ['banana', 'tomato'],
#                   'Meet, Chicken and Fish': ['chest', 'ham'], 'Bread & Bakery': ['rye bread', 'tortilla'],
#                   'Frozen & Salads': ['tivol', 'sandfrost']}
# my_cart = ShoppingCart()
# my_product = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 'small packs')
# my_inventory = InventoryMgmt()
# my_inventory.add_to_stock(my_product, 20)
# my_cart.add_product(my_product, 20)
# my_inventory.remove_from_stock(my_product, 7)
# print my_inventory
# print my_cart
# print my_product


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