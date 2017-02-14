'''
This module defines the class for Payment Option creation.
'''
import sqlite3
import os

class PaymentOption:
    '''
    Purpose:
        This Class handles creation of a Payment Option.

    Methods:
        __init__(self, first_name, last_name, acct_number, exp_date, ccv, category)

    Author:
        @mccordgh
    '''

    def __init__(self, first_name, last_name, acct_number, exp_date, ccv, category):
        self.first_name = first_name
        self.last_name = last_name
        self.acct_number = acct_number
        self.exp_date = exp_date
        self.ccv = ccv
        self.category = category

    def save_to_db(self):
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        INSERT OR IGNORE INTO Payments VALUES (null, "{}", "{}", "{}", "{}", "{}", "{}", 1)
        """.format(self.first_name, self.last_name, self.acct_number, self.exp_date, self.ccv, self.category)

        cursor.execute(sql_command)

        connection.commit()
        connection.close()

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_acct_number(self):
        return self.acct_number

    def get_exp_date(self):
        return self.exp_date

    def get_ccv(self):
        return self.ccv

    def get_category(self):
        return self.category

    def check_if_acct_exists(self):
        connection = sqlite3.connect('{}bangazon.db'.format(self.get_dir_fix()))
        cursor = connection.cursor()

        sql_command = """
        SELECT acct_number 
        FROM Payments 
        WHERE acct_number={}
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
        if os.path.basename(os.getcwd()) == 'tests' or os.path.basename(os.getcwd()) == 'scripts':
            return '../'
        else:
            return ''

