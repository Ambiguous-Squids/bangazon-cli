import os
import sys
import main
sys.path.append('../')
from payment_option import PaymentOption
from superuser import Superuser
from customer import Customer
from product import Product
from order import Order
from session_manager import SessionManager



def completeOrder(active_customer):

    '''
    Complete an order interface
    - If no products have been added to order, return user to main menu
    - Provides order total and 'ready to purchase?' prompt (Y/N)
        if user enters N, mainMenu() to return to main interface
    - Allows superuser to add payment option
    - Calls mainMenu() to return to main interface

    @nchemsak
    '''

    os.system("clear")

    print("\n""******************************* \n"
        "**       Complete Order      ** \n"
        "******************************* \n")



    '''If no products have been selected yet'''
    # self.order.get_products()
    print("Please add some products to your order first. Press any key to return to main menu.")

    # Order.get_total(self)
    ready = input("\nYour order total is $149.54. Ready to purchase (Y/N) > ")

    if ready == 'Y':
        print("\nChoose a payment option:\n")
        input("Your order is complete! Press ENTER to return to main menu.")
        main.mainMenu(active_customer)

    elif ready == 'N':
        main.mainMenu(active_customer)

    else:
        completeOrder(active_customer)


    main.mainMenu(active_customer)
