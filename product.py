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
        self.__name = name
        self.__price = price
        self.__popularity = [(1, 100)]

    def get_popularity(self):
        return self.__popularity

    def set_popularity(self, product_id, quantity):
        pass

