"""
Functions Calling Functions — Exercises

Small functions can call one another to divide a larger task into
clear, reusable steps.
"""


def calculate_total(price, tax):
    """Return price plus tax."""
    return price + tax


def calculate_discount(total, discount):
    """Return total after subtracting a discount."""
    return total - discount


def print_receipt(item, price, tax, discount):
    """Print a receipt using the calculation functions."""
    total = calculate_total(price, tax)
    final_total = calculate_discount(total, discount)

    print(f"Item: {item}")
    print(f"Subtotal: ${price:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Final total: ${final_total:.2f}")


# Exercise 1: One function calls another to calculate a total.
print("Total:", calculate_total(50, 5))


# Exercise 2: Reuse the total in another function.
subtotal = calculate_total(80, 8)
print("After discount:", calculate_discount(subtotal, 10))


# Exercise 3: Build a larger task from smaller functions.
print_receipt("Keyboard", 50, 5, 3)


# Exercise 4: Use helper functions to determine a test result.
def is_within_limit(actual, limit):
    """Return whether actual is no greater than limit."""
    return actual <= limit


def report_response_time(actual, limit):
    """Print a response-time test result."""
    if is_within_limit(actual, limit):
        print(f"PASS: {actual}s is within the {limit}s limit.")
    else:
        print(f"FAIL: {actual}s exceeds the {limit}s limit.")


report_response_time(1.4, 2.0)
report_response_time(2.5, 2.0)


# Exercise 5: A function can call multiple helper functions.
def format_test_name(name):
    """Return a test name with consistent capitalization."""
    return name.strip().title()


def create_test_report(name, actual, limit):
    """Return a formatted test report."""
    clean_name = format_test_name(name)
    passed = is_within_limit(actual, limit)
    status = "Passed" if passed else "Failed"
    return f"{clean_name}: {status} ({actual}s, limit {limit}s)"


print(create_test_report("  login page loads  ", 1.1, 2.0))


# Mock Interview
# Question: Why split a larger function into smaller helper functions?
#
# Answer: Smaller functions each handle one clear task. This makes the
# code easier to read, reuse, test, and maintain.
