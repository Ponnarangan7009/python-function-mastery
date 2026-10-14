"""
12 - First-Class Functions

In Python, functions are objects. You can:
- assign a function to a variable,
- pass a function to another function,
- return a function from another function.
"""


def greet(name):
    """Return a greeting for name."""
    return f"Hello, {name}!"


# Assign a function to another variable (no parentheses)
greeting_function = greet
print(greeting_function("Asha"))


def run_function(function, value):
    """Call the function passed in."""
    return function(value)


# Pass greet as an argument
print(run_function(greet, "Ravi"))


def get_multiplier():
    """Return a function."""
    def multiply_by_two(number):
        return number * 2

    return multiply_by_two


# Store and call the returned function
double = get_multiplier()
print(double(5))
