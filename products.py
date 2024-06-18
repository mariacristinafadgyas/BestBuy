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
        if self.active == True:
            return True
        return False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Please select a positive non-zero number")
        if quantity > self.quantity:
            raise ValueError("Out of stock!")
        total_amount = float(self.price * quantity)
        self.quantity -= quantity
        return total_amount


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(1))
print(bose.quantity)
print(mac.buy(100))
print(mac.is_active())

print(bose.show())
print(mac.show())

bose.set_quantity(1000)
print(bose.show())
print(bose.quantity)
