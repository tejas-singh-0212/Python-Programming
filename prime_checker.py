# defining the function to check prime number
def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num%i==0:
            is_prime = False
    if is_prime:
        print("It\'s a prime number")
    else:
        print("It\'s not a prime number")
# taking user input
number = int(input("Enter a whole number: "))
# function call
prime_checker(number)