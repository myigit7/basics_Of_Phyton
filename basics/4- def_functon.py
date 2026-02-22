"""
def display_invoice (username, amount, due_date): # Variable location's so important when change the location code must be change so be careful for the listing.
    print(f"Hello {username}")
    print(f"Your bill of ${amount: .2f} is due: {due_date}") # amount is float variable so we can write the .2f because after the "." program should write 2 digits.

display_invoice("JoeSchmo", 100.01, "01/02")

"""
def add (x, y):
    z= x + y
    return z


def subtract (x, y):
    z = x - y
    return z


def multiply (x, y):

    z = x * y

    return z

def divide (x, y):

    z = x / y

    return z

print(add(1, 2))

print(divide(1, 2))

print(multiply(1, 2))

print(subtract(1, 2))

def crate_name (first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = crate_name("mehmet", "yigit")

print(full_name)