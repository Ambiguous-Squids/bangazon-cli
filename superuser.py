import sqlite3
from customer import Customer

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

    def get_customers():
        with sqlite3.connect("../bangazon.db") as b:
            cursor = b.cursor()

            try:
                cursor.execute("SELECT c.idCustomer,c.first_name, c.last_name FROM Customers c")
            except sqlite3.OperationalError:
                return False
            customer = cursor.fetchall()
            return customer

