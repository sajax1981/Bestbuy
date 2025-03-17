import pytest
from products import Product


def test_ordering_too_large_quantity():
    """Test ordering more than available quantity should raise ValueError."""
    product = Product("Smartphone", price=700, quantity=10)

    # Trying to buy more than available quantity
    with pytest.raises(ValueError, match="Not enough stock available"):
        product.buy(20)  # Ordering more than available


def test_product_runs_out_of_stock():
    """Test product deactivates when quantity reaches zero."""
    product = Product("Headphones", price=150, quantity=3)

    # Buying all stock
    product.buy(3)

    # After purchasing, the quantity should be 0 and product should be inactive
    assert product.get_quantity() == 0
    assert not product.is_active()  # Should be inactive


def test_invalid_product_parameters():
    """Test invalid product creation raises ValueError."""

    # Creating a product with an empty name
    with pytest.raises(ValueError, match="Invalid input: name cannot be empty, price and quantity cannot be negative"):
        Product("", price=100, quantity=10)

    # Creating a product with a negative price
    with pytest.raises(ValueError, match="Invalid input: name cannot be empty, price and quantity cannot be negative"):
        Product("Laptop", price=-500, quantity=10)

    # Creating a product with a negative quantity
    with pytest.raises(ValueError, match="Invalid input: name cannot be empty, price and quantity cannot be negative"):
        Product("Tablet", price=300, quantity=-5)
