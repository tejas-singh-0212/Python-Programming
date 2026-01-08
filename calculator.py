def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b==0:
        return "Division by zero error"
    return a/b

def mod(a, b):
    if b==0:
        return "Division by zero error"
    return a%b
 
def floor_divide(a, b):
    if b==0:
        return "Division by zero error"
    return a//b

logo = '''
                                 _____________________
                                |  _________________  |
                                | | Python       0. | |
                                | |_________________| |
                                |  ___ ___ ___   ___  |
                                | | 7 | 8 | 9 | | + | |
                                | |___|___|___| |___| |
                                | | 4 | 5 | 6 | | - | |
                                | |___|___|___| |___| |
                                | | 1 | 2 | 3 | | x | |
                                | |___|___|___| |___| |
                                | | . | 0 | = | | / | |
                                | |___|___|___| |___| |
                                |_____________________|
'''
operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "%" : mod,
    "//": floor_divide

}
def calculator():
    print(logo)
    num1 = float(input("Enter first number: "))
    for symbol in operation:
        print(symbol, end="\t")
    should_continue = True
    while should_continue:
        operation_symbol = input("\nPick an operation from the line above: ")
        num2 = float(input("Enter second number: "))
        answer = operation[operation_symbol](num1, num2)
        if operation_symbol in operation:
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        else:
            print("Invalid Input")
        
        if input(f"Type \"y\" to continue calculating with {answer}, or type \"n\" to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()