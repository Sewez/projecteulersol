# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

# Function to return sum of the squares
def sum_squares(numbers):
    square_list = list(map(lambda x: math.pow(x, 2), numbers))
    return sum(square_list)

# Function to return square of the sum
def squares_of_sum(numbers):
    return math.pow(sum(numbers), 2)

# Generate a list of natural numbers from 1 - 100
natural_nums = range(1, 101, 1)
# Print difference
print (squares_of_sum(natural_nums) - sum_squares(natural_nums))

# ANS: 25164150.0