"""
03 - Positional and Keyword Arguments

Positional arguments are matched to parameters by their order.
Keyword arguments are matched by the parameter name.

Keyword arguments make function calls easier to read.
"""


def describe_person(name, role):
    """Print a person's name and role."""
    print(f"{name} works as a {role}.")


# Positional arguments: order determines which value goes where
describe_person("Asha", "tester")

# Keyword arguments: parameter names identify each value
describe_person(role="developer", name="Ravi")
