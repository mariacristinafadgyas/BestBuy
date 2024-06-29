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
            total_quantity += item._quantity
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
            total_price += product.buy(quantity)
        return total_price

    def __contains__(self, product):
        return product in self.list_of_products

    def __add__(self, other):
        combined_products = self.list_of_products + other.list_of_products
        return Store(combined_products)


# import promotions
# import products
# product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
#                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                 products.Product("Google Pixel 7", price=500, quantity=250),
#                 products.NonStockedProduct("Windows License", price=125),
#                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
#                 ]
#
# second_half_price = promotions.SecondHalfPrice("Second Half price!")
# third_one_free = promotions.ThirdOneFree("Third One Free!")
# thirty_percent = promotions.PercentDiscount("30% off!", percent=20)
#
# product_list[0].set_promotion(third_one_free)
# product_list[1].set_promotion(thirty_percent)
# product_list[2].set_promotion(second_half_price)
#
# print(product_list[0].buy(3))
# print(product_list[1].buy(1))
# print(product_list[2].buy(2))
# import products
# mac =  products.Product("MacBook Air M2", price=1450, quantity=100)
# bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# pixel = products.Product("Google Pixel 7", price=500, quantity=250)
#
# best_buy = Store([mac, bose])
# mac.price = -100         # Should give error
# print(mac)               # Should print `MacBook Air M2, Price: $1450 Quantity:100`
# print(mac > bose)        # Should print True
# print(mac < bose)        # Should print True
# print(mac in best_buy)   # Should print True
# print(pixel in best_buy) # Should print False
#
# product1 = products.Product("iPhone", 1450, 100)
# product2 = products.Product("Samsung Galaxy", 1200, 50)
# product3 = products.Product("Google Pixel", 900, 70)
# product4 = products.Product("OnePlus", 600, 30)
# product5 = products.Product("Huawei", 500, 20)
#
# store1 = Store([product1, product2])
# store2 = Store([product3, product4, product5])
#
# # Combine two stores
# combined_store = store1 + store2
