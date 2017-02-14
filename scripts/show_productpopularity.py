import os
import sys
import main
sys.path.append('../')
from product import Product


def show_product_popularity():

    '''
        Show product popularity interface    
        calls mainMenu() to return to main interface

        @asimonia
    '''

    os.system("clear")

    # Create a product
    
    product = Product("A", 1, 1)
    product.print_product_popularity()

    print('\n')
    input("-> Press any key to return to main menu")

    main.mainMenu()

if __name__ == '__main__':
    show_product_popularity()

