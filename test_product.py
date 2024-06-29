import pytest
import products


# Test that creating a normal product works
def test_create_normal_product():
    i_phone = products.Product("iPhone", price=1450, quantity=100)

    assert i_phone.name == "iPhone"
    assert i_phone.price == 1450
    assert i_phone._quantity == 100
    assert i_phone.is_active() is True


# Test that creating a product with invalid details (empty name, negative price) invokes an exception
def test_empty_name():
    with pytest.raises(ValueError, match="Name cannot be empty"):
        products.Product("", price=1450, quantity=100)


def test_negative_price():
    with pytest.raises(ValueError, match="Price cannot be negative"):
        products.Product("MacBook Air M2", price=-10, quantity=100)


def test_negative_quantity():
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        products.Product("MacBook Air M2", price=10, quantity=-100)


# Test that when a product reaches 0 quantity, it becomes inactive.
def test_is_inactive():
    i_phone = products.Product("iPhone", price=1450, quantity=100)
    i_phone.buy(100)

    assert i_phone.is_active()


# Test that product purchase modifies the quantity and returns the right output.
def test_modifies_quantity():
    mac_book = products.Product("MacBook Air M2", price=10, quantity=100)
    mac_book.buy(quantity=10)

    assert mac_book._quantity == 90


# Test that buying a larger quantity than exists invokes exception
def test_larger_quantity_than_in_stock():
    mac_book = products.Product("MacBook Air M2", price=10, quantity=100)

    with pytest.raises(ValueError, match="Out of stock!"):
        mac_book.buy(quantity=200)


pytest.main()


if __name__ == "__main__":
    pytest.main()
