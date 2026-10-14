"""
16 - Generators and yield

A generator produces values one at a time.
The yield keyword pauses the function and remembers its state until
the next value is requested.
"""


def count_up_to(limit):
    """Yield integers from 1 through limit."""
    number = 1
    while number <= limit:
        yield number
        number += 1


for value in count_up_to(3):
    print(value)
