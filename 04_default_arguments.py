"""
04 - Default Arguments

A default argument gives a parameter a value to use when the caller
does not provide one. A caller can still pass a different value.
"""


def greet(name, message="Welcome"):
    """Print a greeting using the default or a supplied message."""
    print(f"{message}, {name}!")


# Uses the default message
greet("Asha")

# Supplies a different message
greet("Ravi", "Good morning")
