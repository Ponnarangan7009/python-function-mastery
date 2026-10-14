"""
functools.wraps — Exercises

functools.wraps preserves metadata from the original function when
a decorator replaces it with a wrapper.
"""

from functools import wraps


# Exercise 1: Compare metadata with and without @wraps.
def decorator_without_wraps(func):
    """A decorator that does not preserve the original metadata."""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decorator_without_wraps
def function_without_wraps():
    """An example function without preserved metadata."""
    return "Done"


print("Without wraps:")
print("Name:", function_without_wraps.__name__)
print("Docstring:", function_without_wraps.__doc__)


# Exercise 2: Preserve the function's name and docstring with @wraps.
def decorator_with_wraps(func):
    """A decorator that preserves the original metadata."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decorator_with_wraps
def function_with_wraps():
    """An example function with preserved metadata."""
    return "Done"


print("\nWith wraps:")
print("Name:", function_with_wraps.__name__)
print("Docstring:", function_with_wraps.__doc__)


# Exercise 3: Use @wraps with a function that accepts arguments.
def log_call(func):
    """Print the function name, then call it."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log_call
def create_test_summary(test_name, status="PASS"):
    """Return a summary for a test."""
    return f"{test_name}: {status}"


print("\nSummary:", create_test_summary("Login test"))
print("Function name:", create_test_summary.__name__)
print("Docstring:", create_test_summary.__doc__)


# Exercise 4: Check that the decorated function's return value is preserved.
@log_call
def add(first, second):
    """Return the sum of two numbers."""
    return first + second


print("\nSum:", add(10, 5))


# Mock Interview
#
# Question: What problem can functools.wraps prevent when writing a
# decorator?
#
# Answer: Without functools.wraps, the wrapper's name and docstring
# replace the original function's metadata. functools.wraps preserves
# that metadata on the decorated function.
