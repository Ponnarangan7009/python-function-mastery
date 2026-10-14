"""
19 - Docstrings and Type Hints

A docstring explains what a module, function, or class does.
Type hints describe the kinds of values a function expects and returns.
Python does not enforce these hints automatically.
"""


def calculate_area(length: float, width: float) -> float:
    """Return the area of a rectangle."""
    return length * width


area = calculate_area(5.0, 3.0)

print("Area:", area)
print("Function docstring:", calculate_area.__doc__)
print("Function annotations:", calculate_area.__annotations__)
