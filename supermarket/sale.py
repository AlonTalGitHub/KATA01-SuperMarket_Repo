from abc import ABCMeta, abstractmethod


# Sale interface
class Sale(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def payment(self, cart):
        # calculate the cart's default price.
        cart_price = 0

        for p in cart.products:
            prod_price = p.full_price * cart.products[p]
            cart_price += prod_price

        return cart_price


class XPercent(Sale):

    def __init__(self, product, percent):
        self.percent_price = product.full_price * percent

    def payment(self, cart):
        return self.percent_price


class OnePlusOne(Sale):

    def __init__(self, buy_this, get_that):
        self.buy_this = buy_this
        self.get_that = get_that

    def payment(self, cart):
        n_buys = cart.products[self.buy_this]
        n_gets = cart.products[self.get_that]
        buy_full_price = self.buy_this.full_price
        get_full_price = self.get_that.full_price

        # if you get the same product.
        if self.buy_this == self.get_that:

            if n_buys % 2 == 0:
                return buy_full_price * n_buys / 2
            n_buys += 1
            return buy_full_price * n_buys / 2

        # if you get other product
        if self.buy_this != self.get_that:

            if n_buys > n_gets:
                cart.products[self.get_that] = n_buys
            if n_buys < n_gets:
                return buy_full_price * n_buys + get_full_price * (n_gets - n_buys)
            return buy_full_price * n_buys