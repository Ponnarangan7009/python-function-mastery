"""
Docstrings and Type Hints — Exercises

Docstrings explain what functions do.
Type hints describe the kinds of values functions expect and return.
Python does not enforce type hints automatically.
"""


# Exercise 1: Add a docstring and type hints to a simple function.
def calculate_area(length: float, width: float) -> float:
    """Return the area of a rectangle."""
    return length * width


area = calculate_area(5.0, 3.0)
print("Area:", area)


# Exercise 2: Use type hints with a string parameter and return value.
def format_test_name(test_name: str) -> str:
    """Return a test name with surrounding whitespace removed."""
    return test_name.strip()


print(format_test_name("  login test  "))


# Exercise 3: Use a bool return type hint.
def is_test_passed(status: str) -> bool:
    """Return whether the test status is PASS."""
    return status == "PASS"


print("Passed:", is_test_passed("PASS"))
print("Passed:", is_test_passed("FAIL"))


# Exercise 4: Use a list type hint.
def count_passed_tests(statuses: list[str]) -> int:
    """Return how many statuses are PASS."""
    return sum(status == "PASS" for status in statuses)


test_statuses = ["PASS", "FAIL", "PASS", "PASS"]
print("Passed test count:", count_passed_tests(test_statuses))


# Exercise 5: Inspect a function's docstring and annotations.
print("Area function docstring:", calculate_area.__doc__)
print("Area function annotations:", calculate_area.__annotations__)


# Mock Interview
#
# Question: Do Python type hints automatically prevent a function from
# receiving a value of the wrong type?
#
# Answer: No. Type hints describe the intended types, but Python does
# not enforce them automatically at runtime. Tools can use the hints to
# help find type-related mistakes.
