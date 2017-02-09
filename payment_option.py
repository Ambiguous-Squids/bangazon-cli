'''
This module defines the class for Payment Option creation.
'''

class PaymentOption:
    '''
    Purpose:
        This Class handles creation of a Payment Optionk.

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
