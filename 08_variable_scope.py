"""
08 - Variable Scope

A local variable is created inside a function and is available there.
A global variable is created outside functions and can be read inside them.

Prefer passing values as parameters and returning results instead of
changing global variables.
"""

message = "I am global"


def show_scope():
    """Show a global variable and a local variable."""
    local_message = "I am local"
    print(message)
    print(local_message)


show_scope()

# The global variable is still available here
print(message)

# local_message is only available inside show_scope()
# Uncommenting the next line causes a NameError:
# print(local_message)
