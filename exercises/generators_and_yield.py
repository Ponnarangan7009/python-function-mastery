"""
Generators and yield — Exercises

A generator yields values one at a time and remembers where it paused.
"""


# Exercise 1: Yield numbers from 1 through a limit.
def count_up_to(limit):
    """Yield integers from 1 through limit."""
    number = 1
    while number <= limit:
        yield number
        number += 1


for value in count_up_to(3):
    print(value)


# Exercise 2: Yield test names one at a time.
def test_name_generator(test_names):
    """Yield each test name from the supplied collection."""
    for test_name in test_names:
        yield test_name


tests = ["login", "search", "payment"]
for test_name in test_name_generator(tests):
    print("Running test:", test_name)


# Exercise 3: Yield only passed test results.
def passed_results(results):
    """Yield results whose status is PASS."""
    for test_name, status in results:
        if status == "PASS":
            yield test_name


test_results = [
    ("login", "PASS"),
    ("search", "FAIL"),
    ("payment", "PASS"),
]

for test_name in passed_results(test_results):
    print("Passed:", test_name)


# Exercise 4: Request generator values with next().
def response_codes():
    """Yield sample HTTP response codes."""
    yield 200
    yield 404
    yield 500


codes = response_codes()
print("First code:", next(codes))
print("Second code:", next(codes))
print("Third code:", next(codes))


# Exercise 5: Compare a generator with a list.
def squares_generator(limit):
    """Yield squares from 1 through limit."""
    for number in range(1, limit + 1):
        yield number * number


print("Squares:", list(squares_generator(5)))


# Mock Interview
#
# Question: What is one difference between a generator and a list?
#
# Answer: A list stores all its values at once. A generator produces
# values one at a time when requested, which can save memory for large
# sequences.
