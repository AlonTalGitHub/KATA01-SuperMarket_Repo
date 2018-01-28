from supermarket.super_market import Cart, Product

product1 = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 'small packs')
product2 = Product(43568, 'Meet & Chicken', 'shnitzel', 43.50, 'kg')
product3 = Product(76768, 'Drinks & Alkohol', 'wain', 55.50, 'bottles')

cart = Cart()
cart.add_product(my_product1, 2)
cart.add_product(my_product2, 3)
cart.add_product(my_product3, 6)