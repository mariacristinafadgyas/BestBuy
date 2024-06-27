class Product:
    """Product class - represents each product with attributes such as name, price, quantity and active status as
    well as methods for managing these attributes"""

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
        return (f"\u001b[38;5;209;1m{self.name}\u001b[0m, Price: \u001b[38;5;199;1m{self.price}\u001b[0m, Quantity: "
                f"\u001b[38;5;199;1m{self.quantity}\u001b[0m")

    def buy(self, quantity) -> float:
        """Returns the total price (float) of a purchase and updates the quantity of the product"""
        if quantity <= 0:
            raise ValueError("\u001b[38;5;9;1mPlease select a positive non-zero number\u001b[0m")
        if quantity > self.quantity:
            raise ValueError("\u001b[38;5;9;1mOut of stock!\u001b[0m")
        total_amount = float(self.price * quantity)
        self.quantity -= quantity
        return total_amount
