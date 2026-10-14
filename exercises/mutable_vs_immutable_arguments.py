"""
Mutable vs Immutable Arguments — Exercises

Lists are mutable: functions can change their contents.
Integers and strings are immutable: rebinding a parameter does not
change the caller's original variable.
"""


def add_item(items, item):
    """Add an item to a list."""
    items.append(item)


def increase_number(number):
    """Increase the local number and return it."""
    number += 1
    return number


def add_tag(text, tag):
    """Return text with a tag appended."""
    text += tag
    return text


# Exercise 1: Observe a function changing a mutable list.
tools = ["Python", "pytest"]
add_item(tools, "Selenium")
print("Tools after adding Selenium:", tools)


# Exercise 2: Observe that rebinding an integer parameter does not
# change the caller's integer.
retry_count = 2
new_retry_count = increase_number(retry_count)
print("Original retry count:", retry_count)
print("Returned retry count:", new_retry_count)


# Exercise 3: Observe that rebinding a string parameter does not
# change the caller's string.
test_name = "Login"
updated_test_name = add_tag(test_name, " test")
print("Original test name:", test_name)
print("Returned test name:", updated_test_name)


# Exercise 4: Avoid changing the input list by making a copy first.
def list_with_item(items, item):
    """Return a new list with item appended."""
    copied_items = items.copy()
    copied_items.append(item)
    return copied_items


original_browsers = ["Chrome", "Firefox"]
updated_browsers = list_with_item(original_browsers, "Edge")
print("Original browsers:", original_browsers)
print("Updated browsers:", updated_browsers)


# Exercise 5: Show that a function can mutate a nested mutable value.
def mark_first_test(tests):
    """Mark the first test as complete."""
    tests[0]["status"] = "Passed"


test_cases = [{"name": "Login", "status": "Not run"}]
mark_first_test(test_cases)
print("Test cases:", test_cases)


# Mock Interview
# Question: If you pass a list to a function and append to it, can the
# caller see the change? What is one way to avoid changing the original?
#
# Answer: Yes. The function can mutate the same list object. Make a copy
# inside the function, then change and return the copy.
