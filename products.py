class Product:
    """Product class - represents each product with attributes such as name,
     price, quantity and active status as well as methods for managing these
      attributes"""

    def __init__(self, name, price, quantity):
        """Creates the instance variables and raises an exception if something is invalid"""
        if not name:
            raise ValueError("\u001b[38;5;9;1mName cannot be empty\u001b[0m")
        if price < 0:
            raise ValueError("\u001b[38;5;9;1mPrice cannot be negative\u001b[0m")
        if quantity < 0:
            raise ValueError("\u001b[38;5;9;1mQuantity cannot be negative\u001b[0m")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> float:
        """Returns the quantity as float"""
        return float(self.quantity)

    def set_quantity(self, quantity):
        """Setter function for quantity. If the quantity is 0 then it deactivates the product"""
        if quantity < 0:
            raise ValueError("\u001b[38;5;9;1mQuantity cannot be 0!\u001b[0m")
        if self.quantity == 0:
            self.deactivate()
        else:
            self.quantity += quantity

    def is_active(self) -> bool:
        """Returns True if the product is active"""
        if self.active:
            return True
        return False

    def activate(self):
        """Activates the product"""
        self.active = True

    def deactivate(self):
        """Deactivates the product"""
        self.active = False

    def show(self):
        """Displays info (name, price and quantity) on screen"""
        if self.promotion:
            promotion_name = self.promotion.get_name()
        else:
            promotion_name = "None"
        return (f"\u001b[38;5;209;1m{self.name}\u001b[0m, Price:"
                f" \u001b[38;5;199;1m${self.price}\u001b[0m, Quantity: "
                f"\u001b[38;5;199;1m{self.quantity}\u001b[0m, Promotion:"
                f" \u001b[38;5;199;1m{promotion_name}\u001b[0m")

    def buy(self, quantity) -> float:
        """Returns the total price (float) of a purchase and updates the quantity of the product"""
        if quantity <= 0:
            raise ValueError("\u001b[38;5;9;1mPlease select a positive non-zero number\u001b[0m")
        if quantity > self.quantity:
            raise ValueError("\u001b[38;5;9;1mOut of stock!\u001b[0m")
        if self.promotion:
            print(self.promotion)
            total_amount = self.promotion.apply_promotion(self, quantity)
        else:
            total_amount = float(self.price * quantity)
        self.quantity -= quantity
        return total_amount

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion


class NonStockedProduct(Product):
    """Product subclass for products that do not require quantity information.
    The quantity attribute is set to 0"""

    def __init__(self, name, price):
        """Uses instance variables of the parent class and sets the quantity to be always 0"""
        super().__init__(name, price, quantity=0)
        self.active = True
        self.promotion = None

    def set_quantity(self, quantity):
        """Raises an error because the subclass does not keep track of
         the quantity"""
        raise NotImplementedError("Quantity cannot be set for non-physical products")

    def buy(self, quantity: int) -> float:
        """Overrides the buy function, as the subclass does not keep track
         of the quantity for this type of product"""
        if self.promotion:
            total_amount = self.promotion.apply_promotion(self, quantity)
        else:
            total_amount = float(self.price * quantity)
        return total_amount

    def show(self):
        """Displays info (name, price & promotion) on screen"""
        if self.promotion:
            promotion_name = self.promotion.get_name()
        else:
            promotion_name = "None"
        return (f"\u001b[38;5;209;1m{self.name}\u001b[0m, Price: "
                f"\u001b[38;5;199;1m${self.price}\u001b[0m, Quantity: "
                f"\u001b[38;5;199;1mUnlimited\u001b[0m, Promotion: "
                f"\u001b[38;5;199;1m{promotion_name}\u001b[0m")


class LimitedProduct(Product):
    """Product subclass for products that can only be purchased once"""

    def __init__(self, name, price, quantity, maximum):
        """Uses instance variables of the parent class and triggers an
         exception if the maximum purchase limit is less than 0"""
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("\u001b[38;5;9;1mMaximum purchase limit must be positive\u001b[0m")
        self.maximum = maximum

    def buy(self, quantity) -> float:
        """Overwrites the buy function, as the subclass enforces a maximum buy limit"""
        if quantity > self.maximum:
            raise ValueError(f"\u001b[38;5;9;1mCannot purchase more than"
                             f" {self.maximum} of this product\u001b[0m")
        if quantity > self.quantity:
            raise ValueError("\u001b[38;5;9;1mNot enough quantity available\u001b[0m")
        if self.promotion:
            total_amount = self.promotion.apply_promotion(self, quantity)
        else:
            total_amount = float(self.price * quantity)
        return total_amount

    def show(self):
        """Displays info (name, price, quantity and maximum purchase) on screen"""
        if self.promotion:
            promotion_name = self.promotion.get_name()
        else:
            promotion_name = "None"
        return (f"\u001b[38;5;209;1m{self.name}\u001b[0m, Price: "
                f"\u001b[38;5;199;1m${self.price}\u001b[0m, Quantity: "
                f"\u001b[38;5;199;1m{self.quantity}\u001b[0m, Limited to "
                f"\u001b[38;5;199;1m1\u001b[0m per order, Promotion: "
                f"\u001b[38;5;199;1m{promotion_name}\u001b[0m")


# windows_licence = NonStockedProduct("Windows License", price=125)
# shipping = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
# print(windows_licence.show())
# print(windows_licence.buy(1))
# print(shipping.show())
