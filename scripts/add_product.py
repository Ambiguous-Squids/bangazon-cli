import os
import sys
import main
sys.path.append('../')
from superuser import Superuser
from product import Product
from order import Order
from customer import Customer
from payment_option import PaymentOption

def addProduct():
    superuser = Superuser()
    products = superuser.get_all_products()

    active_order = Order(
        superuser.get_customer_by_id(2),
        True,
        superuser.get_payment_option_by_id(1)        
        )
    active_order.save_to_db()
    active_order.get_last_order_id()
    
    print(
        "\n"
        "******************************* \n"
        "** Add products to order ** \n"
        "******************************* \n"
        )

    for product in products:
        print("{:<3}{:<20}{:<8}{}".format(product[0], product[1], product[2], product[3]))

    print("\nChoose an item to add to your order or type 'Done' to finish")
    
    item = str(input(">"))
    
    if item != 'Done':
        item = int(item)
        new_product = products[item-1]
        added_product = Product(new_product[1], new_product[2], new_product[3])
        new_customer = Customer(
            "Albert",
            "Einstein",
            "123 Atom Way",
            "Apt. B2",
            "Nashville",
            "TN",
            "32233",
            "615-555-555",
            "bigal@al.com"
            )


        superuser.add_product_to_order(added_product,active_order)
        print('Product added ')
        addProduct()
    else:
        return

def completeOrder():
    print('Do you want to complete order? y/n')
    answer = input(">")



addProduct()

completeOrder()