"""
First-Class Functions — Exercises

Python functions are objects. They can be assigned to variables,
passed as arguments, and returned from other functions.
"""


# Exercise 1: Assign a function to another variable.
def greet(name):
    """Return a greeting."""
    return f"Hello, {name}!"


greeting_function = greet
print(greeting_function("Asha"))


# Exercise 2: Pass a function into another function.
def apply_function(function, value):
    """Call function with value and return the result."""
    return function(value)


def make_uppercase(text):
    """Return text in uppercase."""
    return text.upper()


print(apply_function(make_uppercase, "python"))


# Exercise 3: Pass different functions to the same helper.
def double(number):
    """Return twice the number."""
    return number * 2


def square(number):
    """Return the number squared."""
    return number * number


print("Doubled:", apply_function(double, 5))
print("Squared:", apply_function(square, 5))


# Exercise 4: Return a function from another function.
def get_multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiply(number):
        return number * factor

    return multiply


triple = get_multiplier(3)
print("Tripled:", triple(4))


# Exercise 5: Use a function as a simple test checker.
def is_positive(number):
    """Return whether number is positive."""
    return number > 0


def report_check(check_function, value):
    """Run a check and print its result."""
    result = check_function(value)
    print(f"Check for {value}: {result}")


report_check(is_positive, 8)
report_check(is_positive, -2)


# Mock Interview
# Question: What does it mean that functions are first-class objects?
#
# Answer: Functions can be treated like other values: assigned to
# variables, passed to functions, and returned from functions.
