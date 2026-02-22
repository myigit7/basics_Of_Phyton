"""
List Comprehension = create listin easily.

[expression for value in iterable if condition]

"""

"""
doubles = []

for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)
"""
"""
doubles = [x * 2 for x in range(1, 11)]
print(doubles)
"""
"""
fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut" ]]
print(fruits)
"""
"""
fruits= ["apple", "orange", "banana", "coconut" ]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)
"""


numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0] # if condition
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(positive_nums)
print(negative_nums)
