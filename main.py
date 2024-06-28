import sys
import products
import store
import promotions


def show_menu():
    """Displays the menu"""

    print("""\u001b[38;5;33;1mStore Menu\u001b[0m
\u001b[38;5;67;1m----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
\u001b[0m""")


def delimiter():
    print("\u001b[38;5;199;1m-----------------------------------------------"
          "---------------------------------------\u001b[0m")


def choose_products(product_list):
    """Asks the user to select a desired product and a quantity, return a tuple of
     the selected product and quantity"""

    delimiter()
    for index, product in enumerate(product_list, start=1):
        print(f"{index}. {product.show()}")
    delimiter()

    options = ["1", "2", "3"]
    option_5_selected = False

    while True:
        try:
            shop_product = input("\u001b[38;5;98;1mWhich product # do you want?"
                                 " \u001b[38;5;184m(Press Enter to quit): \u001b[0m")
            if shop_product == "":
                return None, None
            if shop_product in options:
                product_index = int(shop_product) - 1
                selected_product = product_list[product_index]
                try:
                    quantity = int(input("\u001b[38;5;113;1mWhich quantity do you want? \u001b[0m"))
                    if 0 < quantity <= selected_product.quantity:
                        return selected_product, quantity
                    else:
                        print(f"\u001b[38;5;9;1mPlease enter a valid quantity (0 to {selected_product.quantity}"
                              f")\u001b[0m")
                except ValueError:
                    print("\u001b[38;5;9;1mPlease enter a number for the quantity!\u001b[0m")
            elif shop_product == "4":
                product_index = 3
                selected_product = product_list[product_index]
                try:
                    quantity = int(input("\u001b[38;5;113;1mWhich quantity do you want? \u001b[0m"))
                    return selected_product, quantity
                except ValueError:
                    print("\u001b[38;5;9;1mPlease enter a number for the quantity!\u001b[0m")
            elif shop_product == "5":
                if option_5_selected:
                    print("\u001b[38;5;9;1mOption 5 can only be selected once. Please select another option!\u001b[0m")
                    continue
                else:
                    product_index = 4
                    selected_product = product_list[product_index]
                    option_5_selected = True
                    while True:
                        try:
                            quantity = int(input("\u001b[38;5;113;1mWhich quantity do you want? \u001b[0m"))
                            if quantity == 1:
                                return selected_product, quantity
                            else:
                                print(f"\u001b[38;5;9;1mPlease only select 1. The product is limited to"
                                      f" 1 per order\u001b[0m")
                        except ValueError:
                            print("\u001b[38;5;9;1mPlease enter a number for the quantity!\u001b[0m")
            else:
                print("\u001b[38;5;9;1mPlease select a number from 1 to 5\u001b[0m")
        except ValueError:
            print("\u001b[38;5;9;1mPlease try again!\u001b[0m")


def make_order(product_list):
    """Returns the shopping list and updates the quantity of the products"""

    shopping_list = []
    while True:
        shop_product, quantity = choose_products(product_list)
        if shop_product is None and quantity is None:
            break
        shopping_list.append((shop_product, quantity))
        shop_product.buy(quantity)
        # shop_product.set_quantity(quantity)
        print("\u001b[38;5;51;1mProduct added to list!\u001b[0m")
    return shopping_list


def start(product_list, best_buy):
    """Displays the menu and prompts the user to select an application mode"""

    while True:
        try:
            show_menu()
            user_input = int(input("\u001b[38;5;22;1mPlease choose a number: \u001b[0m"))
            if isinstance(user_input, int) and 1 <= user_input <= 4:
                if user_input == 1:
                    delimiter()
                    for index, product in enumerate(product_list, start=1):
                        print(f"{index}. {product.show()}")
                    delimiter()
                elif user_input == 2:
                    delimiter()
                    print(f"\u001b[38;5;148;1mTotal of \u001b[38;5;199;1m{best_buy.get_total_quantity()}\u001b[0m "
                          f"\u001b[38;5;148;1mitems in the store.\u001b[0m")
                    delimiter()
                elif user_input == 3:
                    shopping_list = make_order(product_list)
                    delimiter()
                    print(f"\u001b[38;5;64;1mOrder made! Total payment: \u001b[38;5;213m$"
                          f"{best_buy.order(shopping_list)}\u001b[0m")
                    delimiter()
                elif user_input == 4:
                    sys.exit()
        except ValueError:
            print("\u001b[38;5;9;1mPlease select a number between 1 and 4!!!\u001b[0m")


def main():
    """Set up the initial stock and call up the start function"""

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]
    best_buy = store.Store(product_list)

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    start(product_list, best_buy)


if __name__ == "__main__":
    main()
