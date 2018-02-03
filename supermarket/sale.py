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
            return 0.0
        # if the product is in cart, return the amount that the sale saves.
        full_price = self.product.full_price
        return full_price * cart.products[self.product] * self.percent / 100.0


class OnePlusOne(Sale):

    def __init__(self, buy_this, get_that):
        self.buy_this = buy_this
        self.get_that = get_that

    def apply(self, cart):

        if self.buy_this not in cart.products:
            return 0.0
        # if buy_this in cart, and get_that not, add the get_that to cart and save the price for get_that.
        if self.get_that not in cart.products:
            cart.add_product(self.get_that, cart.products[self.buy_this])

        '''now we have buy_this and get_that in the cart.'''
        # variables names
        n_buys = cart.products[self.buy_this]
        n_gets = cart.products[self.get_that]
        buy_full_price = self.buy_this.full_price
        get_full_price = self.get_that.full_price

        # if you get the same product you are buying.
        if self.buy_this == self.get_that:

            if n_buys % 2 == 0:
                return buy_full_price * n_buys / 2
            n_buys += 1
            return buy_full_price * n_buys / 2

        # if you get other product from the product you are buying.
        if self.buy_this != self.get_that:

            if n_buys > n_gets:
                cart.products[self.get_that] = n_buys
            if n_buys < n_gets:
                return get_full_price * n_buys  # you save only the amount you buy.
            return buy_full_price * n_buys


class XforFix(Sale):
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def apply(self, cart):
        pass

# print 12 % 10.0
# print 12 / int(10.0) 