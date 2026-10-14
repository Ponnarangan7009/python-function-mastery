"""
09 - Mutable vs Immutable Arguments

Lists are mutable, so a function can change the original list.
Integers are immutable, so changing a parameter inside a function
does not change the caller's integer.
"""


def add_item(items):
    """Append an item to the list."""
    items.append("new item")


def increase_number(number):
    """Increase the local number parameter."""
    number += 1
    print("Inside function:", number)


my_items = ["pen", "book"]
add_item(my_items)
print("List after function call:", my_items)

my_number = 10
increase_number(my_number)
print("Number after function call:", my_number)
