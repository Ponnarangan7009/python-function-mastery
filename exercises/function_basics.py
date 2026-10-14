"""
Function Basics — Exercises

Practise defining, calling, and reusing functions.
"""


# Exercise 1: Create and call a function that prints a welcome message.
def show_welcome_message():
    """Print a welcome message."""
    print("Welcome to Python function practice!")


show_welcome_message()


# Exercise 2: Create a function that prints your name.
def show_name():
    """Print a name."""
    print("My name is Alex.")


show_name()


# Exercise 3: Create a function that prints a simple test result.
def show_test_result():
    """Print a sample automation test result."""
    print("Test passed: Login page is displayed.")


show_test_result()


# Exercise 4: Call the same function more than once.
def show_reminder():
    """Print a study reminder."""
    print("Practise a little every day.")


show_reminder()
show_reminder()


# Exercise 5: Define a function without calling it.
# The message below is printed, but the function's message is not,
# because show_unfinished_task() is not called.
def show_unfinished_task():
    """Print a message when this function is called."""
    print("This function runs only when called.")


print("The final function has been defined but not called.")
