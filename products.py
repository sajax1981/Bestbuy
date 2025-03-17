class Product:
    """
    Represents a product in an inventory system with a name, price, quantity, and active status.
    """
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product instance.

        :param name: The name of the product.
        :param price: The price of the product (must be non-negative).
        :param quantity: The quantity of the product (must be non-negative).
        :raises ValueError: If the name is empty or if price/quantity are negative.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input: name cannot be empty, price and quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Returns the current quantity of the product.

        :return: The quantity of the product.
        """
        return self.quantity


    def set_quantity(self, quantity: int):
        """
        Sets the quantity of the product. If the quantity is set to zero, the product is deactivated.

        :param quantity: The new quantity of the product (must be non-negative).
        :raises ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        """
        Checks whether the product is active.

        :return: True if the product is active, False otherwise.
        """
        return self.active


    def activate(self):
        """
        Activates the product, making it available for purchase.
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates the product, making it unavailable for purchase.
        """
        self.active = False


    def show(self) -> str:
        """
        Returns a string representation of the product.

        :return: A formatted string showing the product's name, price, and quantity.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity: int) -> float:
        """
        Purchases a specified quantity of the product.

        :param quantity: The number of units to purchase (must be greater than 0 and within stock).
        :return: The total cost of the purchase.
        :raises ValueError: If quantity is not positive or exceeds available stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price


if __name__ == '__main__':
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
