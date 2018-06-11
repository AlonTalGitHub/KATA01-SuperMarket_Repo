from abc import ABCMeta, abstractmethod


# Sale interface
class Sale(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def apply(self, cart):
        pass


class XPercent(Sale):

    def __init__(self, product, percent):
        self.product = product
        self.percent = percent

    def apply(self, cart):
        if self.product not in cart.products:
            return 0.0, cart
        # if the product is in cart, return the amount that the sale saves.
        current_price = self.product.sale_price
        self.product.sale_price = current_price * (100.0 - self.percent) / 100.0
        return current_price * cart.products[self.product] * self.percent / 100.0


class OnePlusOne(Sale):

    def __init__(self, buy_this, get_that):
        self.buy_this = buy_this
        self.get_that = get_that

    def apply(self, cart):

        if self.buy_this not in cart.products or self.buy_this.units == 'kg':
            return 0.0

        # if buy_this in cart, and get_that not, add the get_that to cart with 0 current_price.
        if self.get_that not in cart.products:
            cart.add_product(self.get_that, cart.products[self.buy_this])
            current_price = self.get_that.sale_price
            self.get_that.sale_price = 0.0

            return cart.products[self.buy_this] * current_price

        '''now the following happens when we have buy_this and get_that in the cart.'''
        # variables names
        n_buys = cart.products[self.buy_this]
        n_gets = cart.products[self.get_that]
        buy_full_price = self.buy_this.sale_price
        get_full_price = self.get_that.sale_price

        # if you get the same product you are buying.
        if self.buy_this == self.get_that:

            if n_buys % 2.0 == 0.0:
                self.buy_this.sale_price /= 2.0
            else:
                cart.products[self.get_that] += 1
                self.buy_this.sale_price /= 2.0

            return self.buy_this.sale_price * cart.products[self.buy_this]

        # if you get other product from the product you are buying.
        if self.buy_this != self.get_that:

            if n_buys > n_gets:
                cart.products[self.get_that] = n_buys
                
            if n_buys < n_gets:
                self.get_that.sale_price *= 1 - (n_buys / float(n_gets))

                return get_full_price * n_buys  # you save only for the amount you're buying.

            self.get_that.sale_price = 0.0

            return buy_full_price * cart.products[self.get_that]


class XforFix(Sale):
    
    def __init__(self, product, min_quantity, price):
        self.product = product
        self.min_quantity = min_quantity
        self.price = price

    def apply(self, cart):

        if self.product not in cart.products or cart.products[self.product] < self.min_quantity:
            return 0.0

        applied_ones = cart.products[self.product] - cart.products[self.product] % self.min_quantity
        pay_applied = self.price * (applied_ones / self.min_quantity)
        pay_fullones = cart.products[self.product] - applied_ones
        pay = pay_applied + pay_fullones
        self.product.sale_price = self.price / self.min_quantity

        saved = self.product.sale_price * cart.products[self.product] - pay

        return saved
