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


def completeOrder(active_customer, order, customer_id):

    superuser = Superuser()
    customer_id = active_customer.get_active_customerId()
    order_id = active_customer.get_active_orderId()

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
    # payments = PaymentOption.get_category()
    payments = superuser.get_all_customer_payments(customer_id)



    print(
        "\n"
        "************************************ \n"
        "**       Complete Your Order      ** \n"
        "************************************ \n")

    '''Order TOTAL and ready to purchase prompt'''
    order_total = order.get_total(order_id)
    ready = input("\nYour order total is ${}. Ready to purchase (Y/N) > ".format(order_total))


    '''Choose Payment Option'''
    if ready == 'Y' or ready == 'y':
        print("\nChoose a payment option:\n")

        for index, payment in enumerate(payments):
            print("\t{}. {:<3} - acct# {:<20}".format((index + 1), payment[6], payment[3]))

        try:
            choice = int(input('>'))

        except:
            print("Please Enter a valid choice as a number only")
            completeOrder(active_customer, order, customer_id)

        payment_type_id = payments[choice - 1][0]
        order.set_payment_type_id(payment_type_id, order_id)
        order.set_status("False", order_id)
        active_customer.set_active_orderId(None)
        input("Your order is complete! Press ENTER to return to main menu.")

    else:
        main.mainMenu(active_customer)

    main.mainMenu(active_customer)

# superuser = Superuser()
# active_customer = SessionManager()
# active_customer.set_active_customerId(2)
# active_customer.set_active_orderId(superuser.get_last_order_id())
# customer_id = active_customer.get_active_customerId()
# active_order = Order(
#         superuser.get_customer_by_id(customer_id),
#         True,
#         None
#         )
# completeOrder(active_customer, active_order, customer_id)
