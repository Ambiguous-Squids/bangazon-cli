import sqlite3
from customer import Customer
from payment_option import PaymentOption
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

    def add_product_to_order(self, product, order, id):
        order.add_product(product, id)

    def get_last_order_id(self):
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        SELECT idOrder MAX
        FROM Orders 
        """

        try:
            cursor.execute(sql_command)
        except: 
            print("ERROR GETTING MAX ORDERID")


        last_order = cursor.fetchall()
        return len(last_order)
        connection.commit()
        connection.close()

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

    def get_customer_by_id(self,id):
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        SELECT * 
        FROM Customers
        WHERE idCustomer={}
        """.format(id)

        try:
            cursor.execute(sql_command)
        except:
            print("************ERROR GETTING CUSTOMER**************")

        results = cursor.fetchall()[0]
        new_customer = Customer(object,results[1],results[2],results[3],results[4],results[5],results[6],results[7],results[8])
        return new_customer

        connection.commit()
        connection.close()

    def get_all_customer_payments(self, customer_id):
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        SELECT * 
        FROM Payments
        WHERE idCustomer={}
        """.format(customer_id)

        try:
            cursor.execute(sql_command)
        except:
            print("************ERROR GETTING ALL PRODUCTS**************")

        results = cursor.fetchall()

        connection.commit()
        connection.close()
            
        return results

    def get_payment_option_by_id(self,id, customer_id):
        print("(*@&#$*(&@#*$&(*@#&$*(@&#*($&@#(*$&(@*#&$*")
        print(self, id, customer_id)
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        SELECT * 
        FROM Payments
        WHERE idPayment={}
        """.format(id)

        try:
            cursor.execute(sql_command)
        except:
            print("************ERROR GETTING PAYMENT OPTION**************")

        results = cursor.fetchall()[0]
        new_payment = PaymentOption(object,results[1],results[2],results[3],results[4],results[5], customer_id)
        return new_payment

        connection.commit()
        connection.close()

    def get_dir_fix(self):
        if os.path.basename(os.getcwd()) == 'tests' or os.path.basename(os.getcwd()) == 'scripts':
            return '../'
        else:
            return ''
    
    def get_customers():
        with sqlite3.connect("../bangazon.db") as b:
            cursor = b.cursor()

            try:
                cursor.execute("SELECT c.idCustomer,c.first_name, c.last_name, c.password FROM Customers c")
            except sqlite3.OperationalError:
                return False
            customer = cursor.fetchall()
            return customer

