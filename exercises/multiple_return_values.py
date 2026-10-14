"""
Multiple Return Values — Exercises

A function can return multiple values separated by commas.
Python packs them into a tuple, which can be unpacked into variables.
"""


# Exercise 1: Return a test's name and status.
def get_test_result():
    """Return a sample test name and status."""
    return "Login test", "Passed"


test_name, test_status = get_test_result()
print("Test:", test_name)
print("Status:", test_status)


# Exercise 2: Return the minimum and maximum from a list.
def get_min_max(numbers):
    """Return the smallest and largest numbers."""
    return min(numbers), max(numbers)


scores = [82, 95, 71, 88]
lowest, highest = get_min_max(scores)
print("Lowest score:", lowest)
print("Highest score:", highest)


# Exercise 3: Return a calculation result and whether it passed a threshold.
def check_response_time(seconds, limit):
    """Return the response time and whether it is within the limit."""
    return seconds, seconds <= limit


response_time, is_within_limit = check_response_time(1.8, 2.0)
print("Response time:", response_time)
print("Within limit:", is_within_limit)
