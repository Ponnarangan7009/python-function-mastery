"""
Default Arguments — Exercises

A default value is used when an argument is omitted.
A caller can provide a different value when needed.
"""


# Exercise 1: Use the default greeting.
def greet(name, message="Welcome"):
    """Print a greeting."""
    print(f"{message}, {name}!")


greet("Asha")


# Exercise 2: Override the default value.
greet("Ravi", "Good morning")


# Exercise 3: Use two default parameters.
def create_test_user(name, role="tester", active=True):
    """Print a summary of a test user."""
    print(f"Name: {name} | Role: {role} | Active: {active}")


create_test_user("Maya")
create_test_user("Dev", role="developer")
create_test_user("Sam", active=False)


# Exercise 4: Use a default timeout in a test helper.
def run_check(check_name, timeout=10):
    """Print the check name and timeout."""
    print(f"Running {check_name} with a {timeout}-second timeout.")


run_check("Login page check")
run_check("Search check", timeout=20)
