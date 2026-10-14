"""
Return vs Print — Exercises

print() displays a value.
return sends a value back so the caller can store or reuse it.
"""


# Exercise 1: This function prints a message but returns no value.
def show_total_with_print(price, tax):
    """Print the total price."""
    print("Total:", price + tax)


printed_result = show_total_with_print(100, 8)
print("Value returned by print-based function:", printed_result)


# Exercise 2: This function returns a value.
def calculate_total(price, tax):
    """Return the total price."""
    return price + tax


total = calculate_total(100, 8)
print("Returned total:", total)


# Exercise 3: Reuse a returned value in another calculation.
discounted_total = calculate_total(100, 8) - 10
print("Total after discount:", discounted_total)


# Exercise 4: Return a test status that can be checked.
def is_status_successful(status):
    """Return True when the status is 'Passed'."""
    return status == "Passed"


login_passed = is_status_successful("Passed")
print("Should the login test pass?", login_passed)
