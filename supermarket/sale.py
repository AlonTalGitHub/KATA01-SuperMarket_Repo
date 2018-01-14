class Sale(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x -y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError('Can not divide by zero!')
        return x / y