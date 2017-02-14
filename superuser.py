import sqlite3
from customer import Customer

class Superuser():

    '''
        Purpose:
            This class handles the superusers actions

        Methods:
            register_customer(self,user)
            user_is_registered(self,user)
            activate_customer(self,user)
            user_is_active(self,user)
            add_product_to_order(self,order,product)

        Author:
            @rtwhitfield84

    '''

    def register_customer(self,customer):
        Customer.register_customer_in_db(self,customer)

    def customer_is_registered(self,customer):
        Customer.customer_is_registered(customer)

    def activate_customer(self,user):
        pass

    def user_is_active(self,user):
        return True

    def add_product_to_order(self, order, product):
        pass
