import sqlite3
from customer import Customer
import os

class Superuser():

    '''
        Purpose:
            This class handles the superusers actions

        Methods:
            register_customer(self,customer)
            user_is_registered(self,customer)
            activate_customer(self,customer)
            user_is_active(self,customer)
            add_product_to_order(self,order,product)

        Author:
            @rtwhitfield84

    '''

    def get_all_products(self):
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        SELECT * 
        FROM Products
        """

        try:
            cursor.execute(sql_command)
        except:
            print("************ERROR GETTING ALL PRODUCTS**************")

        return cursor.fetchall()

        connection.commit()
        connection.close()
            
    def register_payment_option(self, payment_option):
        payment_option.save_to_db()

    def register_customer(self,customer):
        Customer.register_customer_in_db(self,customer)

    def customer_is_registered(self,customer):
        Customer.customer_is_registered(customer)

    def activate_customer(self,customer):
        pass

    def customer_is_active(self,customer):
        return True

    def add_product_to_order(self, order, product):
        pass

    def get_dir_fix(self):
        if os.path.basename(os.getcwd()) == 'tests' or os.path.basename(os.getcwd()) == 'scripts':
            return '../'
        else:
            return ''
