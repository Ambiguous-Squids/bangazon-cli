import sqlite3
import os
import locale

"""
This module defines the class for Product creation.
"""


# Set US for currency formatting
locale.setlocale( locale.LC_ALL, '' )




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
        with sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix())) as bangazon:
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


    def print_product_popularity(self):
        products = self.get_product_popularity_in_db()

        order_total, customers_total, revenue_total = 0, 0, 0

        for product in products:
            order_total += product[1]
            customers_total += product[2]
            revenue_total += product[3]

        print("Product           Orders     Customers  Revenue")
        print("*******************************************************")
        for product in products:
            name, order, customer, revenue = product
            print("{:<18.17}{:<11}{:<11}{:<15}".format(name, order, customer, locale.currency(revenue, grouping=True)))

        print("*******************************************************")
        print("{:<18.17}{:<11}{:<11}{:<15}".format('Totals:', order_total, customers_total, locale.currency(revenue_total, grouping=True)))

    def get_dir_fix(self):
        if os.path.basename(os.getcwd()) == 'tests':
            return '../'
        else:
            return ''


