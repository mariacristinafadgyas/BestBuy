class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        return float(self.quantity)

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be 0!")
        if self.quantity == 0:
            self.deactivate()
        else:
            self.quantity += quantity

    def is_active(self) -> bool:
        if self.active:
            return True
        return False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"\u001b[38;5;209;1m{self.name}\u001b[0m, Price: \u001b[38;5;199;1m{self.price}\u001b[0m, Quantity: \u001b[38;5;199;1m{self.quantity}\u001b[0m"

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Please select a positive non-zero number")
        if quantity > self.quantity:
            raise ValueError("Out of stock!")
        total_amount = float(self.price * quantity)
        self.quantity -= quantity
        return total_amount
