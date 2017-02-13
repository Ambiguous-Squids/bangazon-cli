import sqlite3
"""
This module defines the class for Product creation.
"""

import sqlite3
import os

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
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.popularity = [(1, 100)]
        self.quantity = quantity

    def get_product_id(self):
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        SELECT idProduct
        FROM Products
        WHERE name="{}"
        """.format(self.name)

        try:
            cursor.execute(sql_command)
        except:
            print("************ERROR GETTING PRODUCT ID**************")

        product_id = cursor.fetchall()[0][0]

        connection.commit()
        connection.close()

        return product_id

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

    def get_dir_fix(self):
        if os.path.basename(os.getcwd()) == 'tests':
            return '../'
        else:
            return ''

    def say_hi(self):
        return "HELLOOOOOOOOOOOOOO"

# frisbee = Product("Frisbee", 49, 345)
# print(frisbee)
# print(frisbee.name)
# print(frisbee.say_hi())
# print(frisbee.get_product_id())
