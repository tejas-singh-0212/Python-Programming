class MoneyMachine:

    CURRENCY = "₹"

    NOTE_VALUES = {
        "₹500 notes": 500,
        "₹200 notes": 200,
        "₹100 notes": 100,
        "₹50 notes": 50,
        "₹20 notes": 20,
        "₹10 notes": 10
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_notes(self):
        """returns the total calculated from notes inserted."""
        print("Please insert money:")
        for note in self.NOTE_VALUES:
            self.money_received += int(input(f"How many {note}?: ")) * self.NOTE_VALUES[note]
        return self.money_received

    def make_payment(self, cost):
        """returns true when payment is accepted, or False if insufficient"""
        self.process_notes()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
