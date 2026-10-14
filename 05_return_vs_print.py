"""
05 - Return vs Print

print() displays a value in the terminal.
return sends a value back to the code that called the function.

Returned values can be stored or used in further calculations.
"""


def add_and_print(a, b):
    """Add two numbers and display the result."""
    print(a + b)


def add_and_return(a, b):
    """Add two numbers and return the result."""
    return a + b


# This function displays the result but does not return it
print("Using print:")
result_from_print = add_and_print(3, 4)
print("Stored result:", result_from_print)

# This function returns a result that can be stored and reused
print("\nUsing return:")
result_from_return = add_and_return(3, 4)
print("Stored result:", result_from_return)
print("Result used in another calculation:", result_from_return * 2)
