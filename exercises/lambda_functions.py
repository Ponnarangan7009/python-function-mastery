"""
Lambda Functions — Exercises

A lambda is a small anonymous function written as one expression.
Syntax: lambda parameters: expression
"""


# Exercise 1: Use a lambda to square a number.
square = lambda number: number * number
print("Square of 5:", square(5))


# Exercise 2: Use a lambda to add two numbers.
add = lambda first, second: first + second
print("Sum:", add(4, 7))


# Exercise 3: Sort test results by duration.
test_results = [
    ("Login", 1.4),
    ("Search", 0.9),
    ("Checkout", 2.1),
]

sorted_results = sorted(test_results, key=lambda result: result[1])
print("Tests sorted by duration:", sorted_results)


# Exercise 4: Sort names by their last character.
names = ["Maya", "Ravi", "Asha", "Dev"]
sorted_names = sorted(names, key=lambda name: name[-1])
print("Names sorted by last character:", sorted_names)


# Exercise 5: Use a lambda with max() to find the slowest test.
slowest_test = max(test_results, key=lambda result: result[1])
print("Slowest test:", slowest_test)


# Exercise 6: Compare a lambda with a regular named function.
def double(number):
    """Return twice the given number."""
    return number * 2


double_lambda = lambda number: number * 2

print("Using def:", double(6))
print("Using lambda:", double_lambda(6))


# Mock Interview
# Question: When is a lambda useful, and when should you use def instead?
#
# Answer: A lambda is useful for a short, one-expression operation,
# often passed to another function such as sorted(). Use def when the
# logic needs multiple statements, a descriptive reusable name, or a
# docstring.
