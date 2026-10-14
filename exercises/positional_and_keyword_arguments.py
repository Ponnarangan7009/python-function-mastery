"""
Positional and Keyword Arguments — Exercises

Positional arguments are matched by order.
Keyword arguments are matched by parameter name.
"""


def create_user(name, role, active):
    """Print a simple user summary."""
    print(f"Name: {name} | Role: {role} | Active: {active}")


# Exercise 1: Call the function using positional arguments.
create_user("Asha", "tester", True)


# Exercise 2: Call it using keyword arguments in a different order.
create_user(active=False, role="developer", name="Ravi")


# Exercise 3: Use a mix of positional and keyword arguments.
# Positional arguments must come before keyword arguments.
create_user("Maya", active=True, role="Python learner")


# Exercise 4: Demonstrate a keyword argument making a call easier to read.
def report_result(test_name, status, duration):
    """Print a test result."""
    print(f"{test_name}: {status} in {duration} seconds")


report_result(
    test_name="Login test",
    status="Passed",
    duration=1.24,
)
