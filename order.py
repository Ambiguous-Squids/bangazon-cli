class Order():

    def __init__(self, customer):
        self.customer = customer
        self.products = []
        self.active = True
        self.total = 0

    def get_customer(self):
        return self.customer

    def add_product(self, product):
        self.products.append(product)
        self.total = self.total + product.price

    def get_products(self):
        return self.products

    def set_status(self, status):
        self.active = status

    def get_status(self):
        return self.active

    def get_total(self):
        return self.total
    