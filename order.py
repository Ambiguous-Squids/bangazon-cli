"""This module defines the class for Order creation"""
import sqlite3
import os

class Order():
    """
    Purpose:
        This class handles creation of a new Order.

    Methods:
        __init__(self, customer)
        add_product(self, product)
        add_payment_option(self, payment_option)
        check_if_order_exists(self)
        get_customer(self)
        get_dir_fix(self)
        get_order_id(self)
        get_products(self)
        save_to_db(self)
        set_status(self)
        get_total(self)
        set_status(self, status)

    Author:
        @alirk / @mccordgh
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

        prod_id = product.get_product_id()
        ord_id = self.get_order_id()

        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        INSERT INTO OrderItems
        VALUES (null, "{}", "{}")
        """.format(ord_id, prod_id)

        try:
            cursor.execute(sql_command)
        except:
            print("************ERROR ADDING TO MANY TO MANY DB**************")        

        connection.commit()
        connection.close()

    def get_order_id(self):
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        SELECT idOrder
        FROM Orders
        WHERE idCustomer=1
        -- AND active="True"
        """

        try:
            cursor.execute(sql_command)
        except:
            print("************ERROR GETTING ORDER ID**************")

        order_id = cursor.fetchall()[0][0]
        
        connection.commit()
        connection.close()

        return order_id

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

        connection.commit()
        connection.close()

        return returned_products

    def set_status(self, status):
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
            UPDATE Orders
            SET active='{}'
            WHERE idOrder=1; 
            """.format(status)

        cursor.execute(sql_command)

        connection.commit()
        connection.close()

    def get_status(self):
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
            SELECT active
            FROM Orders
            WHERE idOrder=1
            """

        cursor.execute(sql_command)
        returned_fetch = cursor.fetchall()

        connection.commit()
        connection.close()

        return returned_fetch[0][0]

    def get_total(self):
        order_total = 0
        for product in self.products:
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