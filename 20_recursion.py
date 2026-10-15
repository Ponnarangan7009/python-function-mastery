"""
20 - Recursion

Recursion is when a function calls itself to solve a smaller version
of a problem.

A recursive function needs:
1. A base case that stops the calls.
2. A recursive call that moves toward the base case.
3. A way to use the result when the call returns.

Each active call has its own frame on Python's call stack.
That is different from a closure.
"""


# 1. Countdown: recursion that performs an action
def countdown(number):
    """Print numbers down to 1, then stop."""
    if number <= 0:  # Base case
        print("Done!")
        return

    print(number)
    countdown(number - 1)  # Recursive step


countdown(3)
# Output:
# 3
# 2
# 1
# Done!


# 2. Sum from 1 through number
def sum_to(number):
    """Return the sum of integers from 1 through number."""
    if number < 0:
        raise ValueError("number must be zero or greater")

    if number == 0:  # Base case
        return 0

    return number + sum_to(number - 1)


print("sum_to(4):", sum_to(4))  # 10


# 3. Factorial
def factorial(number):
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("number must be zero or greater")

    if number == 0:  # Base case: 0! is 1
        return 1

    return number * factorial(number - 1)


print("factorial(4):", factorial(4))  # 24


# 4. Count items in a list
def count_items(items):
    """Return the number of items in a list."""
    if not items:  # Base case: an empty list has zero items
        return 0

    return 1 + count_items(items[1:])


print("count_items:", count_items(["login", "payment", "search"]))  # 3


# 5. Sum the values in a list
def sum_list(numbers):
    """Return the sum of the numbers in a list."""
    if not numbers:  # Base case: the sum of an empty list is zero
        return 0

    return numbers[0] + sum_list(numbers[1:])


print("sum_list:", sum_list([4, 7, 2]))  # 13


# 6. Count passed test results
def count_passed_tests(results):
    """Return how many test results have the status PASS."""
    if not results:
        return 0

    current_count = 1 if results[0] == "PASS" else 0
    return current_count + count_passed_tests(results[1:])


test_results = ["PASS", "FAIL", "PASS", "SKIP"]
print("Passed tests:", count_passed_tests(test_results))  # 2


# 7. Sum the digits of a non-negative integer
def sum_digits(number):
    """Return the sum of the digits in a non-negative integer."""
    if number < 0:
        raise ValueError("number must be non-negative")

    if number < 10:  # Base case: one digit remains
        return number

    last_digit = number % 10
    remaining_digits = number // 10
    return last_digit + sum_digits(remaining_digits)


print("sum_digits(472):", sum_digits(472))  # 13


# 8. Reverse a string
def reverse_text(text):
    """Return text with its characters in reverse order."""
    if not text:  # Base case: the string is empty
        return ""

    return reverse_text(text[1:]) + text[0]


print("reverse_text:", reverse_text("cat"))  # tac


# 9. Fibonacci: branching recursion with two recursive calls
def fibonacci(number):
    """Return the Fibonacci value at a non-negative position."""
    if number < 0:
        raise ValueError("number must be non-negative")

    if number == 0:
        return 0
    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


print("fibonacci(12):", fibonacci(12))  # 144


# Remember:
# - Check that every recursive call moves toward a base case.
# - Trace a small input by hand when the calls feel confusing.
# - This simple Fibonacci version repeats calculations, so use it only
#   for small inputs.
