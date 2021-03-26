class ShoppingCart(object):
    def __init__(self) -> None:
        self.cart = {}

    def add(self, name, price, quantity):
        item = self.cart.get(name)
        if item:
            item["price"] = price
            item["quantity"] += quantity
        else:
            self.cart[name] = dict(price=price, quantity=quantity)

    def remove(self, name):
        item = self.cart.get(name)
        if item:
            if item["quantity"] > 1:
                item["quantity"] -= 1
            else:
                self.cart.pop(name)

    def total(self):
        return print(
            f"Total: {sum([value.get('price') for name, value in self.cart.items()])}"
        )


if __name__ == "__main__":
    sc = ShoppingCart()
    sc.add("book", 30, 1)  # name, price-per-unit, quantity
    sc.add("toothbrush", 3, 4)

    sc.remove("toothbrush")  # removes one toothbrush -- or removes

    sc.total()  # returns the total price of items in the shopping cart