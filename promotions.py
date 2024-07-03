from abc import ABC, abstractmethod
import products


class Promotion(ABC):
    """Abstract class for store promotions"""
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class PercentDiscount(Promotion):
    """Subclass of the abstract class Promotion, which implements a
     percentage discount"""

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        total_price = product.price * quantity
        discount_amount = total_price * (self.percent / 100)
        return total_price - discount_amount


class SecondHalfPrice(Promotion):
    """Subclass of the abstract class Promotion, which implements a 50%
     discount for the second product purchased"""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        promo = (quantity // 2) * (product.price / 2)
        return (quantity * product.price) - promo


class ThirdOneFree(Promotion):
    """Subclass of the abstract class Promotion, which implements a
     "buy 2, get 1 free" discount"""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        full_price_items = (2 * (quantity // 3)) + (quantity % 3)
        total_price = full_price_items * product.price
        return total_price

def main():
    win_license = products.NonStockedProduct("Windows License", price=125)
    shipping = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    second_half_price = SecondHalfPrice("Second Half price!")
    win_license.set_promotion(second_half_price)
    print(win_license)
    print(win_license.buy(2))
    print(shipping)
    print(shipping.buy(2))

if __name__ == "__main__":
    main()