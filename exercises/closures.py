"""
Closures — Exercises

A closure is an inner function that remembers values from its
enclosing function, even after the enclosing function has returned.
"""


# Exercise 1: Create a function that remembers a multiplier.
def make_multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiply(number):
        return number * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print("Double 6:", double(6))
print("Triple 6:", triple(6))


# Exercise 2: Create a greeting function that remembers a greeting.
def make_greeter(greeting):
    """Return a function that uses the remembered greeting."""
    def greet(name):
        return f"{greeting}, {name}!"

    return greet


say_hello = make_greeter("Hello")
say_good_morning = make_greeter("Good morning")

print(say_hello("Asha"))
print(say_good_morning("Ravi"))


# Exercise 3: Create a counter with a remembered value.
def make_counter():
    """Return a function that increases and remembers a count."""
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


login_attempts = make_counter()
print("Attempts:", login_attempts())
print("Attempts:", login_attempts())
print("Attempts:", login_attempts())


# Exercise 4: Make separate counters with independent state.
search_attempts = make_counter()
print("Search attempts:", search_attempts())
print("Login attempts:", login_attempts())


# Mock Interview
# Question: What makes an inner function a closure?
#
# Answer: It remembers and can use values from its enclosing scope,
# even after the enclosing function has finished running.
