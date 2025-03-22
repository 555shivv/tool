class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product_name):
        for item in self.items:
            if item["product"].name == product_name:
                self.items.remove(item)
                return
        print(f"{product_name} is not in the cart.")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def print_receipt(self):
        print("Shopping Cart Receipt:")
        for item in self.items:
            print(f"{item['product'].name} - {item['quantity']} - ${item['product'].price * item['quantity']}")
        print(f"Total: ${self.calculate_total()}")


def test_shopping_cart():
    product1 = Product("Apple", 0.5)
    product2 = Product("Banana", 0.4)
    product3 = Product("Orange", 0.6)

    cart = ShoppingCart()

    cart.add_item(product1, 2)
    cart.add_item(product2, 3)
    cart.add_item(product3, 1)

    assert len(cart.items) == 3
    assert cart.calculate_total() == 2 * 0.5 + 3 * 0.4 + 1 * 0.6

    cart.remove_item("Banana")
    assert len(cart.items) == 2
    assert cart.calculate_total() == 2 * 0.5 + 1 * 0.6

    cart.remove_item("Banana")  # Trying to remove an item that doesn't exist
    assert len(cart.items) == 2

    print("Shopping Cart Tests Passed!")


def main():
    test_shopping_cart()
    apple = Product("Apple", 0.5)
    banana = Product("Banana", 0.4)
    orange = Product("Orange", 0.6)

    cart = ShoppingCart()

    cart.add_item(apple, 2)
    cart.add_item(banana, 3)
    cart.add_item(orange, 1)

    cart.print_receipt()


if __name__ == "__main__":
    main()

