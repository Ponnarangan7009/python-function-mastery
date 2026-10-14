"""
18 - Positional-Only and Keyword-Only Parameters

Parameters before / are positional-only.
Parameters after * are keyword-only.
"""


def describe_item(name, /, price, *, currency="USD"):
    """Show positional-only, regular, and keyword-only parameters."""
    print(f"{name}: {price:.2f} {currency}")


# name must be positional; currency must be passed by keyword
describe_item("Notebook", 4.50, currency="USD")
