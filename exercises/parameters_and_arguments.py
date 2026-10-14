"""
Parameters and Arguments — Exercises

A parameter is a name in a function definition.
An argument is a value supplied when calling the function.
"""


# Exercise 1: Define a function with one parameter and call it with two names.
def greet_person(name):
    """Print a greeting for the given name."""
    print(f"Hello, {name}!")


greet_person("Asha")
greet_person("Ravi")


# Exercise 2: Define a function with two parameters.
def introduce_person(name, role):
    """Print a person's name and role."""
    print(f"{name} works as a {role}.")


introduce_person("Maya", "Python learner")


# Exercise 3: Pass a value stored in a variable as an argument.
city = "Chennai"
greet_person(city)


# Exercise 4: Return a value based on a parameter.
def square_number(number):
    """Return the square of a number."""
    return number * number


result = square_number(6)
print("Square:", result)


# Exercise 5: Use a parameter in a simple testing message.
def report_test_status(test_name, status):
    """Print a test name and its status."""
    print(f"{test_name}: {status}")


report_test_status("Login test", "Passed")
