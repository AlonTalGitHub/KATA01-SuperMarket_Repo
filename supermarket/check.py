from supermarket.sale import XPercent, OnePlusOne, XforFix
from supermarket.super_market import Product, Cart, Inventory


# products.
product1 = Product(73459, 'Milk & Eggs', 'yammy eggs', 10.0, 10.0, 'small packs')
product2 = Product(43568, 'Meet & Chicken', 'shnitzel', 10.0, 10.0, 'packs')
product3 = Product(76768, 'Drinks & Alkohol', 'wain', 10.0, 10.0, 'bottles')

inventory = Inventory()

inventory.add_to_stock(product1, 100)
inventory.add_to_stock(product2, 100)
inventory.add_to_stock(product3, 100)

cart1 = Cart()
cart1.add_product(product1, 2)
cart1.add_product(product2, 3)
cart1.add_product(product3, 6)

xpercent = {product1: 30, product2: 20}
one_plus_one = {product1: product3}
x_for_fix = {product2: [2, 16.0]}
print one_plus_one[product1]

# add the product to cart from the barcode.
def bar_to_product(barcode, cart):

    for product in inventory.stock.keys():
        if barcode == product.barcode:
            cart.add_product(product, 1)
            return cart
    return cart

# check for sales in the cart.
def check_for_sales(cart):
    # cart is empty.
    if cart == Cart():
        return 0.0, cart

    saved = 0.0

    for product in cart.products:
        if product in xpercent:
            saved += XPercent(product, xpercent[product]).apply(cart)

    for product in cart.products:
        if product in one_plus_one:
            saved += OnePlusOne(product, one_plus_one[product]).apply(cart)

    for product in cart.products:
        if product in x_for_fix:
            min_quantity = x_for_fix[product][0]
            price = x_for_fix[product][1]
            saved += XforFix(product, min_quantity, price).apply(cart)

    print saved, cart
    return saved, cart

# run.
barcode2 = 43568

bar_to_product(barcode2, cart1)
check_for_sales(cart1)