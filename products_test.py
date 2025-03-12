import pytest
import products

def test_product_store():
    # Create test products
    product1 = products.Product("MacBook Air M2", price=1450, quantity=100)
    product2 = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    product3 = products.Product("Google Pixel 7", price=500, quantity=250)

    # Test ordering a quantity too large
    with pytest.raises(ValueError, match="Not enough stock available"):
        product1.purchase(200)  # Trying to buy more than available

    # Test product that runs out of stock
    product3.purchase(250)  # Buy all stock
    assert product3.quantity == 0  # Ensure it's out of stock

    # Test product2 ordering within stock
    product2.purchase(100)  # Buy 100 units
    assert product2.quantity == 400  # Ensure stock is updated

    # Test creating a product with invalid parameters
    with pytest.raises(ValueError, match="Invalid price or quantity"):
        products.Product("Invalid Product", price=-10, quantity=5)  # Negative price

    with pytest.raises(ValueError, match="Invalid price or quantity"):
        products.Product("Another Invalid", price=100, quantity=-1)  # Negative quantity
