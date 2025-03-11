class Product:

    def __init__(self, name: str, price: float, quantity: int):

        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input: name cannot be empty, price and quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:

        return self.quantity

    def set_quantity(self, quantity: int):

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:

        return self.active

    def activate(self):

        self.active = True

    def deactivate(self):

        self.active = False
    def show(self) -> str:

        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:

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
