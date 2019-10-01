# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Function to return true or false if evenly divisible
def is_evenly_div(value, div_by):
    if value % div_by == 0:
        return True
    else:
        return False

# Function to check if /value is evenly divisbile by /range_list
def check_evenly_div_range(value, range_list):
    for x in range_list:
        if is_evenly_div(value, x) == False: 
            return False
    
    # /Value is evenly divisible by all values in /range_list
    return True

start_value = 1

while check_evenly_div_range(start_value, range(1, 21, 1)) == False:
    start_value += 1

print start_value

# Solution 232792560