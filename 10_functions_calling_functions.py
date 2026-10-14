"""
10 - Functions Calling Functions

A function can call another function to reuse its behavior.
Breaking a task into small functions makes code easier to read and maintain.
"""


def calculate_total(price, tax):
    """Return the price plus tax."""
    return price + tax


def print_receipt(item, price, tax):
    """Calculate and print a simple receipt."""
    total = calculate_total(price, tax)
    print(f"Item: {item}")
    print(f"Price: ${price:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")


print_receipt("Notebook", 4.50, 0.45)

