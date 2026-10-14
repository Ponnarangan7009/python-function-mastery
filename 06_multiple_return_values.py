"""
06 - Multiple Return Values

A function can return multiple values separated by commas.
Python packs them into a tuple, which can be unpacked into variables.
"""


def get_min_max(numbers):
    """Return the smallest and largest numbers."""
    return min(numbers), max(numbers)


values = [8, 3, 12, 5]

# Unpack the two returned values into separate variables
smallest, largest = get_min_max(values)

print("Numbers:", values)
print("Smallest:", smallest)
print("Largest:", largest)
