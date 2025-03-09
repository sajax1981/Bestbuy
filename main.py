import products
import store

product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)


def start(store_obj):
    """
    Starts the user interface for managing the store.

    :param store_obj: An instance of the Store class.
    """
    while True:
        print("\nStore Menu
        print("\n----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number\n")

        if choice == "1":
            print("\nAvailable Products")
            for product in store_obj.get_all_products():
                print(product.show())

        elif choice == "2":
            print(f"\nTotal quantity in store:, {store_obj.get_total_quantity()} "
                  f"items ")

        elif choice == "3":
            shopping_list = []
            products_list = store_obj.get_all_products()

            print("\nAvailable Products:")
            for i, product in enumerate(products_list, start=1):
                print(f"{i}. {product.show()}")

            while True:
                try:
                    product_index = int(input("\nEnter the product number to buy? ")) - 1
                    if product_index == -1:
                        break

                    if product_index < 0 or product_index >= len(products_list):
                        print("Invalid product selection, try again.")
                        continue

                    quantity = int(input(f"Enter quantity for {products_list[product_index].name}: "))
                    if quantity <= 0:
                        print("Quantity must be greater than 0. Try again.")
                        continue

                    shopping_list.append((products_list[product_index], quantity))

                except ValueError:
                    print("Invalid input! Please enter a valid number.")

            if shopping_list:
                try:
                    total_cost = store_obj.order(shopping_list)
                    print(f"\nOrder placed successfully! Total cost: ${total_cost:.2f}")
                except ValueError as e:
                    print(f"Order failed: {e}")

        elif choice == "4":
            print("\nThank you for visiting Best Buy! Goodbye! 👋")
            break

        else:
            print("\nInvalid choice! Please select a valid option (1-4).")


if __name__ == '__main__':
    start(best_buy)
