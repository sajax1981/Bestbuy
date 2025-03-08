import products

class Store:
    def __init__(self, products):
        self.products =[]
        self.total_quantity = 0

    def add_product(self, product):
        self.products.append(product)
        self.total_quantity += product.get_quantity()

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            self.total_quantity -= product.get_quantity()

    def get_total_quantity(self) -> int:
        total_quantity = sum(p.get_quantity() for p in self.products)
        return total_quantity

    def get_all_products(self):
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list) -> float:
        total_cost = 0.0
        for product, quantity in shopping_list:
            if quantity > product.get_quantity():
                raise ValueError(f"Not enough stock for {product.name}.")
            total_cost += product.buy(quantity)
        return total_cost

if __name__ == "__main__":
    # Create some Product instances
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)

    # Create the Store instance with initial products
    best_buy = Store([bose, mac])

    # Order example with a shopping list: 5 Bose Earbuds, 30 MacBooks, and 10 more Bose Earbuds
    price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])

    print(f"Order cost: {price} dollars.")

