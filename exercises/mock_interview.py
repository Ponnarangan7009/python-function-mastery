"""
Python Functions — Mock Interview Practice

Read each question, try answering it aloud, then compare your answer.
"""


# 1. What is a function?
# A reusable block of code that performs a task. Define it with def
# and call it by using its name followed by parentheses.


# 2. What is the difference between a parameter and an argument?
# A parameter is a name in a function definition. An argument is the
# value supplied when the function is called.


# 3. What is the difference between positional and keyword arguments?
# Positional arguments are matched by order. Keyword arguments are
# matched by parameter name.


# 4. What is a default parameter value?
# It is a value used when the caller omits that argument.


# 5. What is the difference between print and return?
# print displays a value. return sends a value back to the caller so
# the program can store or use it.


# 6. Can a function return more than one value?
# Yes. Python packs comma-separated return values into a tuple, which
# can be unpacked into separate variables.


# 7. What do *args and **kwargs collect?
# *args collects extra positional arguments into a tuple.
# **kwargs collects extra keyword arguments into a dictionary.


# 8. What is variable scope?
# Scope is where a variable can be accessed. A local variable belongs
# to a function; a global variable is defined outside functions.


# 9. What happens when a function changes a list passed to it?
# Lists are mutable, so changes to the list's contents can be seen by
# the caller. Copy the list first if the original should remain unchanged.


# 10. What does it mean that functions are first-class objects?
# Functions can be assigned to variables, passed to other functions,
# and returned from functions.


# 11. What is a lambda function?
# A small anonymous function written as one expression. Use def when
# the logic needs multiple statements or a descriptive reusable name.


# 12. What is a closure?
# An inner function that remembers values from its enclosing scope,
# even after the enclosing function has finished.


# 13. What is a decorator?
# A function that takes another function and returns a function with
# added or changed behavior.


# 14. What does functools.wraps do?
# It preserves metadata such as the original function's name and
# docstring on the decorator's wrapper.


# 15. What does yield do?
# It produces a value from a generator and pauses the function, which
# can continue from that point when another value is requested.


# 16. What is a generator expression?
# A lazy expression that produces values one at a time. It resembles a
# list comprehension but uses parentheses.


# 17. What do / and * mean in a function signature?
# Parameters before / are positional-only. Parameters after * are
# keyword-only. Parameters between them can be passed either way.


# 18. Are Python type hints enforced automatically?
# No. They describe intended types and can be checked by tools, but
# Python does not enforce them automatically at runtime.


# 19. How would you count passed tests?
# Iterate over the statuses and count the values equal to "PASS", or
# use sum(status == "PASS" for status in statuses).


# 20. How would you make a decorator support different function
# arguments?
# Define its wrapper with *args and **kwargs, then call the original
# function as func(*args, **kwargs).


# 21. Why avoid a mutable list as a default argument?
# The same list object is reused across calls. Use None as the default,
# then create a new list inside the function when needed.


# 22. How can one function use another function's result?
# Call the helper function, store or use its returned value, and pass
# that value to the next operation.


# Practice tip:
# Try answering each question aloud without reading the comments.
# Then explain one small code example for each answer.
