"""This module defines the class for Order creation"""

class Order():
    """
    Purpose:
        This class handles creation of a new Order.

    Methods:
        __init__(self, customer)
        get_customer(self)
        add_product(self, product)
        get_products(self)
        set_status(self, status)
        get_total(self)

    Author:
        @alirk
    """

    def __init__(self, customer):
        self.customer = customer
        self.products = []
        self.active = True
        self.total = 0

    def get_customer(self):
        return self.customer

    def add_product(self, product):
        self.products.append(product)
        self.total = self.total + product.price

    def get_products(self):
        return self.products

    def set_status(self, status):
        self.active = status

    def get_status(self):
        return self.active

    def get_total(self):
        return self.total
    