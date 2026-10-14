"""
Positional-Only and Keyword-Only Parameters — Exercises

Parameters before / are positional-only.
Parameters after * are keyword-only.
Parameters between / and * can be positional or keyword arguments.
"""


# Exercise 1: Use a positional-only parameter.
def greet(name, /):
    """Return a greeting for name."""
    return f"Hello, {name}!"


print(greet("Asha"))
# greet(name="Asha") would raise a TypeError because name is positional-only.


# Exercise 2: Use a keyword-only parameter.
def run_test(test_name, *, browser):
    """Return a message describing the test and browser."""
    return f"Running {test_name} on {browser}"


print(run_test("login", browser="Chrome"))
# run_test("login", "Chrome") would raise a TypeError because browser is keyword-only.


# Exercise 3: Use positional-only, regular, and keyword-only parameters.
def describe_item(name, /, price, *, currency="USD"):
    """Return a description of an item and its price."""
    return f"{name}: {price:.2f} {currency}"


print(describe_item("Notebook", 4.50, currency="USD"))
print(describe_item("Keyboard", price=25.00, currency="EUR"))


# Exercise 4: Make test helper calls clear with a keyword-only option.
def check_response_time(test_name, seconds, *, limit=2.0):
    """Return whether a test's response time is within its limit."""
    passed = seconds <= limit
    status = "PASS" if passed else "FAIL"
    return f"{test_name}: {status} ({seconds}s, limit {limit}s)"


print(check_response_time("login", 1.4))
print(check_response_time("search", 2.5, limit=2.0))


# Mock Interview
#
# Question: What do / and * mean in a function parameter list?
#
# Answer: Parameters before / can only be passed positionally.
# Parameters after * can only be passed by keyword. Parameters between
# them may be passed positionally or by keyword.
