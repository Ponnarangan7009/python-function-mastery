"""
11 - Lambda Functions

A lambda is a small anonymous function written in one expression.

Syntax:
    lambda parameters: expression

Use a regular def function for more complex logic or when a function
needs a descriptive name.
"""

# A regular function
def square(number):
    return number * number


# The same operation written as a lambda
square_lambda = lambda number: number * number

print("Using def:", square(5))
print("Using lambda:", square_lambda(5))

# Lambdas are often useful for short operations passed to other functions
numbers = [5, 2, 8, 1]
sorted_numbers = sorted(numbers, key=lambda number: number)

print("Sorted numbers:", sorted_numbers)
