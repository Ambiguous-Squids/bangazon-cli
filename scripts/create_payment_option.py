import os
import sys
import main
sys.path.append('../')
from payment_option import PaymentOption
from superuser import Superuser


def createPaymentOption(active_customer):

    '''
        Payment option creation interface
        provides inputs to enter payment option information
        passes inputs to superuser method 
        to register a payment option in db
        calls mainMenu() to return to main interface

        @mccordgh
    '''

    os.system("clear")
    id_customer = active_customer.get_active_customerId()

    print(
        "\n"
        "******************************* \n"
        "** Create a Payment Option   ** \n"
        "******************************* \n"
        )


    print("\nEnter payment option first name")
    first_name = str(input(">"))

    print("\nEnter payment option last name")
    last_name = str(input(">"))

    print("\nEnter account number")
    acct_number = str(input(">"))

    print("\nEnter expiration date")
    exp_date = str(input(">"))

    print("\nEnter CCV #")
    ccv = str(input(">"))

    print("\nEnter category (VISA, AMEX, MASTERCARD, etc)")
    category = str(input(">"))

    new_payment_option = PaymentOption(
        first_name,
        last_name,
        acct_number,
        exp_date,
        ccv,
        category,
        id_customer
        )
    
    Superuser.register_payment_option(object, new_payment_option)
    main.mainMenu(active_customer)
