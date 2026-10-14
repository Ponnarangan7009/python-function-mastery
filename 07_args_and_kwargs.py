"""
07 - *args and **kwargs

*args collects extra positional arguments into a tuple.
**kwargs collects extra keyword arguments into a dictionary.
"""


def show_scores(*args):
    """Display all positional scores."""
    print("Scores:", args)


def show_profile(**kwargs):
    """Display keyword details."""
    print("Profile:", kwargs)


# Extra positional arguments are collected into a tuple
show_scores(85, 92, 78)

# Extra keyword arguments are collected into a dictionary
show_profile(name="Asha", role="tester", experience=2)
