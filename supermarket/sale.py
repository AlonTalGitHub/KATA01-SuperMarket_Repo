class PercentOffSale(object):

    def __init__(self, product, percent):
        self.percent_price = product.full_price * percent
