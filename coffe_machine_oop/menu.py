class MenuItem:
    """models each menu item"""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """models the menu with drinks"""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=25, cost=200),
            MenuItem(name="espresso", water=50, milk=0, coffee=20, cost=120),
            MenuItem(name="cappuccino", water=250, milk=100, coffee=25, cost=250),
        ]

    def get_items(self):
        """returns the available items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """searches the menu for a drink by name. returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
