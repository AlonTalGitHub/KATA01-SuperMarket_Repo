from supermarket.super_market import ShoppingCart, Product

my_product1 = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 'small packs')
my_product2 = Product(43568, 'Meet & Chicken', 'shnitzel', 43.50, 'kg')
my_product3 = Product(76768, 'Drinks & Alkohol', 'wain', 55.50, 'bottles')

my_cart = ShoppingCart()
my_cart.add_product(my_product1, 2)
my_cart.add_product(my_product2, 3)
my_cart.add_product(my_product3, 6)