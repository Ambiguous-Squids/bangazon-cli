import sqlite3
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

    def get_product_popularity_in_db(self):
        with sqlite3.connect("../bangazon.db") as bangazon:
            cursor = bangazon.cursor()

            try:
                cursor.execute("""
                    SELECT *
                    FROM ProductPopularity
                """)
            except sqlite3.OperationalError:
                print("Could not query ProductPopularity table")
                return False

            product_popularity = cursor.fetchall()
            return product_popularity

    def set_popularity(self, product_id, quantity):
        pass

