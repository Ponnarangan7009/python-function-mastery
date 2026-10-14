"""
Decorators — Practice Exercises

These exercises practise writing and applying decorators, preserving
function metadata, handling arguments, and changing or controlling
function behavior.
"""

from functools import wraps


# Exercise 1: Apply a decorator manually
#
# Write a decorator called log_execution that:
# 1. Accepts a function.
# 2. Defines a wrapper with no arguments.
# 3. Prints "Before test".
# 4. Calls the original function.
# 5. Prints "After test".
# 6. Returns the original function's result.
# 7. Returns the wrapper.
#
# Apply the decorator manually, without using @.
#
# Expected output:
# Before test
# Executing payment test
# After test
# PASS


def log_execution(func):
    """Print messages before and after calling a function."""
    def wrapper():
        print("Before test")
        result = func()
        print("After test")
        return result

    return wrapper


def payment_test():
    """Print a message and return the payment test status."""
    print("Executing payment test")
    return "PASS"


payment_test = log_execution(payment_test)
payment_status = payment_test()
print(payment_status)


# Exercise 2: Decorate a function that accepts arguments
#
# Write a decorator called log_test_execution that:
# 1. Accepts a function.
# 2. Uses a wrapper that accepts positional and keyword arguments.
# 3. Prints "Test started" before calling the function.
# 4. Passes all arguments to the original function.
# 5. Prints "Test finished" after the function returns normally.
# 6. Returns the original function's result.
# 7. Preserves the original function's metadata.
#
# Expected output:
# Test started
# Testing login for tester on Chrome
# Test finished
# Test started
# Testing login for admin on Firefox
# Test finished


def log_test_execution(func):
    """Log the start and finish of a test function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Test started")
        result = func(*args, **kwargs)
        print("Test finished")
        return result

    return wrapper


@log_test_execution
def login_test(username, browser="Chrome"):
    """Print which user and browser are being tested."""
    print(f"Testing login for {username} on {browser}")
    return "PASS"


tester_status = login_test("tester")
admin_status = login_test(username="admin", browser="Firefox")


# Exercise 3: Change a string result to uppercase
#
# Write a decorator called uppercase_result that:
# 1. Supports positional and keyword arguments.
# 2. Calls the original function normally.
# 3. Converts a string result to uppercase.
# 4. Returns non-string results unchanged.
# 5. Preserves the original function's metadata.
#
# Do not change the decorated functions' implementations.


def uppercase_result(func):
    """Convert a string returned by func to uppercase."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result

    return wrapper


@uppercase_result
def get_greeting(name):
    """Return a greeting for a person."""
    return f"Hello, {name}"


@uppercase_result
def get_status(service, environment="production"):
    """Return the current service status."""
    return f"{service} is running in {environment}"


print(get_greeting("Karthi"))
print(get_status("payment", environment="staging"))


# Exercise 4: Count calls to a decorated function
#
# Write a decorator called count_calls that:
# 1. Works with functions that accept different arguments.
# 2. Keeps a separate call count for each decorated function.
# 3. Increments and prints the count on each call, as "Call 1",
#    "Call 2", and so on.
# 4. Calls the original function and preserves its return value.
# 5. Preserves the original function's metadata.


def count_calls(func):
    """Print how many times the decorated function has been called."""
    call_count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print(f"Call {call_count}")
        return func(*args, **kwargs)

    return wrapper


@count_calls
def add(first, second):
    """Return the sum of two numbers."""
    return first + second


print(add(1, 10))
print(add(2, 20))
print(add(3, 30))


# Exercise 5: Run a function only when a condition is true
#
# Write a decorator factory called run_only_if that:
# 1. Accepts a Boolean condition.
# 2. Returns a decorator.
# 3. Runs the decorated function when the condition is True.
# 4. Prints "Execution skipped" and returns None when it is False.
# 5. Supports positional and keyword arguments.
# 6. Preserves the decorated function's metadata.


def run_only_if(condition):
    """Create a decorator that runs a function only if condition is true."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)

            print("Execution skipped")
            return None

        return wrapper

    return decorator


@run_only_if(True)
def greet(name):
    """Return a greeting."""
    return f"Hello, {name}!"


@run_only_if(False)
def calculate_total(first, second):
    """Return the sum of two numbers."""
    return first + second


print(greet("Karthik"))
print(calculate_total(10, 100))


# Exercise 6: Allow only positive integers
#
# Write a decorator called positive_numbers_only that:
# 1. Checks every positional argument before calling the function.
# 2. Accepts only positive integers. Remember that bool is a subclass
#    of int, so True must not count as a valid integer here.
# 3. Returns "Invalid arguments" without calling the function if any
#    positional argument is invalid.
# 4. Supports keyword arguments, which do not need validation.
# 5. Preserves the decorated function's metadata.


def positive_numbers_only(func):
    """Call func only when all positional arguments are positive ints."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        are_valid = all(type(value) is int and value > 0 for value in args)

        if not are_valid:
            return "Invalid arguments"

        return func(*args, **kwargs)

    return wrapper


@positive_numbers_only
def multiply(first, second):
    """Return the product of two values."""
    return first * second


print(multiply(1, 5))
print(multiply(1, -5))
print(multiply(1, True))


# Exercise 7: Cache results for positional arguments
#
# Write a decorator called cache_result that:
# 1. Stores results from previous calls.
# 2. Returns the stored result when called again with the same
#    positional arguments, without calling the original function.
# 3. Stores different arguments as separate entries.
# 4. Preserves the decorated function's metadata.
# 5. May assume all positional arguments are hashable.
# 6. Does not need to support keyword arguments.


def cache_result(func):
    """Cache results using each call's positional arguments as a key."""
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)

        return cache[args]

    return wrapper


@cache_result
def calculate_square(number):
    """Return the square of a number."""
    print(f"Calculating square for {number}")
    return number * number


print(calculate_square(5))
print(calculate_square(6))
print(calculate_square(5))


# Mock Interview
#
# Question: What does functools.wraps do in a decorator?
#
# Answer: functools.wraps copies important metadata from the original
# function to the wrapper, including its name and docstring. This makes
# the decorated function easier to inspect and document.
