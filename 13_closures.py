"""
13 - Closures

A closure is an inner function that remembers values from the
enclosing function, even after the enclosing function has finished.
"""


def make_multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiply(number):
        return number * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print("Double 5:", double(5))
print("Triple 5:", triple(5))
