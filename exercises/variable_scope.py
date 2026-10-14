"""
Variable Scope — Exercises

Local variables are created inside functions.
Global variables are created outside functions.
Prefer parameters and return values over changing globals.
"""


# Exercise 1: Read a global variable inside a function.
project_name = "Python Function Mastery"


def show_project_name():
    """Print the global project name."""
    print("Project:", project_name)


show_project_name()


# Exercise 2: Create and use a local variable.
def show_test_message():
    """Create and print a local variable."""
    message = "Running the login test"
    print(message)


show_test_message()


# Exercise 3: Return a local value so it can be used outside.
def create_status():
    """Return a local status value."""
    status = "Passed"
    return status


test_status = create_status()
print("Returned status:", test_status)


# Exercise 4: Pass a value into a function instead of relying on a global.
def report_test(test_name, status):
    """Print the supplied test name and status."""
    print(f"{test_name}: {status}")


report_test("Search test", "Passed")


# local_message exists only inside show_test_message().
# Uncommenting the next line would raise a NameError:
# print(message)
