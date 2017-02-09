"""
This module defines the class for Product creation.
"""

class Product():
    """
    Purpose:
        This class handles creation of a product.
    
    Methods:
        __init__(self)
        get_popularity(self)
        set_popularity(self, product_id, quantity)

    Author:
        @alirk, @asimonia
    """
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.popularity = [(1, 100)]

    def get_popularity(self):
        return self.popularity

    def set_popularity(self, product_id, quantity):
        pass

