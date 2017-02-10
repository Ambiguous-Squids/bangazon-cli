"""This module defines the class for Order creation"""
import sqlite3
import os

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

    def __init__(self, customer, products, active, payment_option, total):
        self.customer = customer
        self.payment_option = payment_option
        self.products = products
        self.active = active

    def get_customer(self):
        return self.customer

    def add_product(self, product):
        self.products.append(product)

    def get_products(self):
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
            SELECT p.name
            FROM Products p, OrderItems o
            WHERE o.idOrder=1
            AND p.idProduct=o.idProduct
            """

        cursor.execute(sql_command)
        returned_fetch = cursor.fetchall()

        returned_products = []
        for product_tupled in returned_fetch:
            for product in product_tupled:
                returned_products.append(product)

        return returned_products

    def set_status(self, status):
        self.active = status

    def get_status(self):
        return self.active

    def get_total(self):
        order_total = 0
        for product in self.products:
            print("{}: ${}".format(product.name, product.price))
            order_total += product.price

        return order_total

    def add_payment_option(self, payment_option):
        self.payment_option = payment_option

    def save_to_db(self):
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        INSERT OR IGNORE INTO Orders VALUES (null, "{}", 1)
        """.format(self.active)

        cursor.execute(sql_command)

        connection.commit()
        connection.close()

    def check_if_order_exists(self):        
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        SELECT idOrder 
        FROM Orders 
        WHERE idCustomer=1
        """.format(self.acct_number)

        try:
            cursor.execute(sql_command)
        except: 
            return False

        acct_info = cursor.fetchall()

        connection.commit()
        connection.close()

        return True

    def get_dir_fix(self):
        if os.path.basename(os.getcwd()) == 'tests':
            return '../'
        else:
            return ''

    def is_active(self):        
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        SELECT active 
        FROM Orders 
        WHERE idCustomer=1
        """

        try:
            cursor.execute(sql_command)
        except: 
            return False

        acct_info = cursor.fetchall()

        connection.commit()
        connection.close()

        return True


connection = sqlite3.connect('bangazon.db')
cursor = connection.cursor()

# sql_command = """
#     SELECT name
#     FROM Products
#     WHERE idProduct = (
#         SELECT idProduct
#         FROM OrderItems
#         WHERE idOrder=1
#         )
#     """

