"""
17 - Generator Expressions

A generator expression creates values lazily, one at a time.
It uses parentheses and resembles a list comprehension.
"""


numbers = [1, 2, 3, 4, 5]

squares_generator = (number * number for number in numbers)

print("Squares:")
for square in squares_generator:
    print(square)
