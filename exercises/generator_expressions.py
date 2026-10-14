"""
Generator Expressions — Exercises

A generator expression creates values lazily, one at a time.
It resembles a list comprehension but uses parentheses.
"""


# Exercise 1: Generate squares lazily.
numbers = [1, 2, 3, 4, 5]
squares = (number * number for number in numbers)

for square in squares:
    print(square)


# Exercise 2: Generate only passed test names.
test_results = [
    ("login", "PASS"),
    ("search", "FAIL"),
    ("payment", "PASS"),
]

passed_names = (
    test_name
    for test_name, status in test_results
    if status == "PASS"
)

print("Passed tests:", list(passed_names))


# Exercise 3: Use a generator expression with sum().
response_times = [0.8, 1.5, 2.0, 1.1]
total_milliseconds = sum(seconds * 1000 for seconds in response_times)
print("Total milliseconds:", total_milliseconds)


# Exercise 4: Use a generator expression with any() and all().
statuses = ["PASS", "PASS", "FAIL"]

has_failure = any(status == "FAIL" for status in statuses)
all_passed = all(status == "PASS" for status in statuses)

print("Has failure:", has_failure)
print("All passed:", all_passed)


# Exercise 5: A generator expression is consumed as it is iterated.
squares_again = (number * number for number in range(1, 4))

print("First value:", next(squares_again))
print("Remaining values:", list(squares_again))


# Mock Interview
#
# Question: Why might you use a generator expression instead of a list
# comprehension?
#
# Answer: A generator expression produces each value only when needed,
# so it can use less memory when processing a large sequence.
