class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_bill(self):
        return sum(item.price for item in self.items)

# Usage
burger = MenuItem("Burger", 120)
coffee = MenuItem("Coffee", 80)

order = Order()
order.add_item(burger)
order.add_item(coffee)

print("Total Bill:", order.total_bill())
