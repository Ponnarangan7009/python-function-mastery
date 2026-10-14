"""
14 - Decorators

A decorator is a function that takes another function, adds behavior,
and returns a function.

The @decorator_name syntax applies a decorator to a function.
"""


def announce(func):
    """Print a message before calling func."""
    def wrapper():
        print("Starting the function...")
        func()
        print("Function finished.")

    return wrapper


@announce
def say_hello():
    print("Hello!")


say_hello()
