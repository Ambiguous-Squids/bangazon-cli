import os
import sys
import main
sys.path.append('../')
from superuser import Superuser

def addProduct():
    superuser = Superuser()
    products = superuser.get_all_products()

    os.system("clear")

    print(
        "\n"
        "******************************* \n"
        "** Add products to order ** \n"
        "******************************* \n"
        )

    for product in products:
        print("{:<3}{:<20}{:<8}{}".format(product[0], product[1], product[2], product[3]))

addProduct()