import os
import sys
import main
sys.path.append('../')
from superuser import Superuser
from product import Product
from order import Order
import complete_an_order
from session_manager import SessionManager

def startOrder(active_customer):
    os.system("clear")
    superuser = Superuser()
    products = superuser.get_all_products()
    customer_id = active_customer.get_active_customerId()

    active_order = Order(
        superuser.get_customer_by_id(customer_id),
        True,
        None
        )
    active_order.save_to_db(None, customer_id)
    active_customer.set_active_orderId(superuser.get_last_order_id())
    products_added = 0  
    addProduct(active_customer, superuser, products, active_order, products_added)

def addProduct(active_customer, superuser, products, active_order, products_added):
    os.system("clear")
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
        superuser.add_product_to_order(added_product,active_order,active_customer.get_active_orderId())
        products_added += 1
        addProduct(active_customer, superuser, products, active_order, products_added)
    else:
        if products_added > 0:
            complete_an_order.completeOrder(active_customer, active_order, active_customer.get_active_customerId())
        else:
            input("Please add some products to your order first. Press enter key to return to main menu.")
            main.mainMenu(active_customer)

# superuser = Superuser()
# active_customer = SessionManager()
# active_customer.set_active_customerId(3)
# active_customer.set_active_paymentId(3)
# startOrder(active_customer)
