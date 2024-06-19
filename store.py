class Store:
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        return self.list_of_products.append(product)

    def remove_product(self, product):
        return self.list_of_products.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for item in self.list_of_products:
            total_quantity += item.quantity
        return total_quantity

    def get_all_products(self):
        active_products = []
        for product in self.list_of_products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
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
