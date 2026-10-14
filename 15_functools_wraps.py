"""
15 - functools.wraps

functools.wraps preserves a decorated function's metadata, such as its
name and docstring. Without it, the wrapper's metadata replaces them.
"""

from functools import wraps


def announce(func):
    """Print a message before calling func."""
    @wraps(func)
    def wrapper():
        print("Starting the function...")
        result = func()
        print("Function finished.")
        return result

    return wrapper


@announce
def say_hello():
    """Return a greeting."""
    print("Hello!")
    return "Greeting complete"


say_hello()

print("Function name:", say_hello.__name__)
print("Docstring:", say_hello.__doc__)
