import products


class Store:
    """
    Represents a store that manages a collection of products.
    Allows adding/removing products, checking total quantity,
    retrieving available products, and processing orders.
    """

    def __init__(self, product_list):
        """
        Initializes the store with a list of products.

        :param product_list: List of Product objects to be managed by the store.
        """
        self.products = product_list

    def add_product(self, product):
        """
        Adds a product to the store's inventory.

        :param product: Product object to add.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store's inventory if it exists.

        :param product: Product object to remove.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculates and returns the total quantity of all products in the store.

        :return: Total quantity of all products.
        """
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self):
        """
        Retrieves a list of all active products in the store.

        :return: List of active Product objects.
        """
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list) -> float:
        """
        Processes an order by deducting stock and calculating the total cost.

        :param shopping_list: List of tuples (Product, quantity) representing the order.
        :return: Total cost of the order.
        :raises ValueError: If any product does not have enough stock.
        """
        total_cost = 0.0
        for product, quantity in shopping_list:
            if quantity > product.get_quantity():
                raise ValueError(f"Not enough stock for {product.name}.")

            # Deduct quantity and calculate cost
            product.set_quantity(product.get_quantity() - quantity)
            total_cost += product.price * quantity
        return total_cost


if __name__ == "__main__":
    available_products = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(available_products)
    store_products = best_buy.get_all_products()
    print(f"Total quantity in store:, {best_buy.get_total_quantity()} items")
    print("Total cost of order:", best_buy.order([(store_products[0], 1), (store_products[1], 2)]))