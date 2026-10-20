"""
Recursion — Exercises

A recursive function calls itself to solve a smaller version of a
problem. Each example includes a solution you can run and review.
"""


# Exercise 1: Add the numbers from 1 through n.
def sum_to(number):
    """Return the sum of integers from 1 through number."""
    if number < 0:
        raise ValueError("number must be zero or greater")

    if number == 0:
        return 0

    return number + sum_to(number - 1)


print("Sum from 1 to 4:", sum_to(4))  # 10


# Exercise 2: Calculate a factorial.
def factorial(number):
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("number must be zero or greater")

    if number == 0:
        return 1

    return number * factorial(number - 1)


print("Factorial of 4:", factorial(4))  # 24


# Exercise 3: Count the items in a list.
def count_items(items):
    """Return the number of items in a list."""
    if not items:
        return 0

    return 1 + count_items(items[1:])


print("Number of items:", count_items(["login", "payment", "search"]))  # 3


# Exercise 4: Add all values in a list.
def sum_list(numbers):
    """Return the sum of the numbers in a list."""
    if not numbers:
        return 0

    return numbers[0] + sum_list(numbers[1:])


print("List sum:", sum_list([4, 7, 2]))  # 13


# Exercise 5: Count test results with the status PASS.
def count_passed_tests(results):
    """Return how many test results have the status PASS."""
    if not results:
        return 0

    current_count = 1 if results[0] == "PASS" else 0
    return current_count + count_passed_tests(results[1:])


test_results = ["PASS", "FAIL", "PASS", "SKIP"]
print("Passed tests:", count_passed_tests(test_results))  # 2


# Exercise 6: Add only the positive numbers in a list.
def sum_positive_numbers(numbers):
    """Return the sum of positive values in a list."""
    if not numbers:
        return 0

    current_value = numbers[0] if numbers[0] > 0 else 0
    return current_value + sum_positive_numbers(numbers[1:])


print("Sum of positive numbers:", sum_positive_numbers([3, -2, 5, 0]))  # 8


# Exercise 7: Add the digits of a non-negative integer.
def sum_digits(number):
    """Return the sum of the digits in a non-negative integer."""
    if number < 0:
        raise ValueError("number must be non-negative")

    if number < 10:
        return number

    last_digit = number % 10
    remaining_digits = number // 10
    return last_digit + sum_digits(remaining_digits)


print("Sum of digits in 472:", sum_digits(472))  # 13


# Exercise 8: Reverse a string.
def reverse_text(text):
    """Return the text with its characters in reverse order."""
    if not text:
        return ""

    return reverse_text(text[1:]) + text[0]


print("Reversed text:", reverse_text("cat"))  # tac


# Exercise 9: Find a Fibonacci number.
def fibonacci(number):
    """Return the Fibonacci value at a non-negative position."""
    if number < 0:
        raise ValueError("number must be non-negative")

    if number == 0:
        return 0
    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


print("Fibonacci number at position 12:", fibonacci(12))  # 144


# Mock Interview
#
# 1. What is recursion?
# A function-solving approach where a function calls itself to solve
# a smaller version of a problem.
#
# 2. What is a base case?
# The simplest case that can be answered directly and stops recursion.
#
# 3. What is the recursive case?
# The part that calls the function again with a smaller problem.
#
# 4. What happens if recursion never reaches its base case?
# Calls keep accumulating until Python raises RecursionError.
#
# 5. How does recursion remember unfinished work?
# Each active call has its own frame on Python's call stack. This is
# different from a closure, which remembers values from an enclosing
# function.
#
# 6. Why can the simple recursive Fibonacci function be slow?
# It recalculates the same Fibonacci values many times. Its running
# time grows exponentially, and the call stack grows with the input.
#
# 7. When might a loop be a better choice?
# A loop is often simpler for straightforward repetition and avoids
# building up recursive calls on the call stack.


# Additional practice: four recursion problems

# Exercise 10: Sum the digits of a non-negative integer.
def sum_of_digits(number):
    """Return the sum of the digits in a non-negative integer."""
    if number < 0:
        raise ValueError("number must be non-negative")
    if number < 10:
        return number
    return number % 10 + sum_of_digits(number // 10)


# Exercise 11: Calculate a non-negative integer power.
def power(base, exponent):
    """Return base raised to exponent using recursive multiplication."""
    if exponent < 0:
        raise ValueError("exponent must be non-negative")
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


# Exercise 12: Reverse a string.
def reverse_string(text):
    """Return text in reverse order using recursion."""
    if len(text) <= 1:
        return text
    return text[-1] + reverse_string(text[:-1])


# Exercise 13: Check whether a string is a palindrome.
def is_palindrome(text):
    """Return whether text reads the same from both ends (case-sensitive)."""
    def check_ends(left, right):
        if left >= right:
            return True
        if text[left] != text[right]:
            return False
        return check_ends(left + 1, right - 1)

    return check_ends(0, len(text) - 1)


print("Sum of digits in 472:", sum_of_digits(472))  # 13
print("2 to the power of 5:", power(2, 5))  # 32
print("Reversed string:", reverse_string("hello"))  # olleh
print("Is 'level' a palindrome?", is_palindrome("level"))  # True


# Try these cases too:
# sum_of_digits(0) == 0
# power(7, 0) == 1
# reverse_string("") == ""
# is_palindrome("python") is False
# is_palindrome("") is True
