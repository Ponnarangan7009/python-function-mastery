"""
*args and **kwargs — Exercises

*args collects extra positional arguments into a tuple.
**kwargs collects extra keyword arguments into a dictionary.
"""


# Exercise 1: Accept any number of test durations.
def show_durations(*durations):
    """Print all supplied test durations."""
    print("Durations:", durations)


show_durations(1.2, 0.8, 2.1)


# Exercise 2: Calculate the total of any number of scores.
def total_scores(*scores):
    """Return the sum of all supplied scores."""
    return sum(scores)


print("Total score:", total_scores(80, 90, 85))


# Exercise 3: Accept named user details.
def show_user_details(**details):
    """Print each user detail."""
    for key, value in details.items():
        print(f"{key}: {value}")


show_user_details(name="Asha", role="tester", active=True)


# Exercise 4: Combine regular parameters, *args, and **kwargs.
def report_run(suite_name, *test_names, **options):
    """Print a test suite, its tests, and run options."""
    print("Suite:", suite_name)
    print("Tests:", test_names)
    print("Options:", options)


report_run(
    "Login checks",
    "valid login",
    "invalid password",
    browser="Chrome",
    headless=True,
)
