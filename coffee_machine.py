# Coffee Menu
menu = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":20
        },
        "cost":120
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":25
        },
        "cost": 200
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":25
        },
        "cost":250
    }
}

profit = 0

# Machine Resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def show_report():
    """
    Shows the report of available resources
    """
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} gm")
    print(f"Money: Rs. {profit}")

def is_resource_sufficient(order_ingriedients):
    """
    Checks if available resources are enough for the order
    """
    for item in order_ingriedients:
        if order_ingriedients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_money():
    """
    Returns the total calculated from the money inserted
    """
    print("Please insert money: ")
    total = int(input("How many ₹500 notes: "))*500
    total += int(input("How many ₹200 notes: "))*200
    total += int(input("How many ₹100 notes: "))*100
    total += int(input("How many ₹50 notes: "))*50
    total += int(input("How many ₹20 notes: "))*20
    total += int(input("How many ₹10 notes: "))*10
    return total

def is_transaction_successful(money_received, drink_cost):
    """
    Returns True is payment accepted, return False if money is insufficient
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ₹{change} in change.")
        global profit
        profit += drink_cost
        return True
    print("Sorry that\'s not enough money.\nMoney refunded.")
    return False

def make_coffee(drink_name, order_ingredients):
    """
    Deduct the required ingredients from the resources
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} 🍵.")

is_on = True
while is_on:
    choice = input("What would you like? (Espresso / Latte / Cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        show_report()
    else:
        if is_resource_sufficient(menu[choice]["ingredients"]):
            payment = process_money()
            if is_transaction_successful(payment, menu[choice]["cost"]):
                make_coffee(choice, menu[choice]['ingredients'])