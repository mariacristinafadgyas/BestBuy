class Store:
    """The Store class is initialised by a list of products and contains methods for adding and removing products,
    for retrieving the total quantity of items, for retrieving all active products and for processing orders."""

    def __init__(self, list_of_products):
        """Creates the instance variable list of products"""
        self.list_of_products = list_of_products

    def add_product(self, product):
        """Adds a product to the store"""
        return self.list_of_products.append(product)

    def remove_product(self, product):
        """Removes a product from store"""
        return self.list_of_products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many products are in the store in total"""
        total_quantity = 0
        for item in self.list_of_products:
            total_quantity += item.quantity
        return total_quantity

    def get_all_products(self):
        """Returns all products in the store that are active"""
        active_products = []
        for product in self.list_of_products:
            if product.is_active():
                active_products.append(product)
        return active_products

    @staticmethod
    def order(shopping_list) -> float:
        """Gets a list of tuples and returns the total price of the order"""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.price * quantity
        return total_price

# product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
#                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                 products.Product("Google Pixel 7", price=500, quantity=250),
#                 ]
#
# store = Store(product_list)
# products = store.get_all_products()
# print(store.get_total_quantity())
# print(store.order([(products[0], 1), (products[1], 2)]))
