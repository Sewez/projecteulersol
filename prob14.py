# Problem 14 >> https://projecteuler.net/problem=14

def is_even(num):
    if num % 2 == 0:
        return True

    return False

def formula_even(num):
    return num / 2

def formula_odd(num):
    return (3 * num) + 1

def run_collatz(num):
    if is_even(num):
        return formula_even(num)
    else:
        return formula_odd(num)

START_NUMBER = 13
# List to hold the number and chain size
MAX_CHAIN = [0, 0]
counter = 0

for x in range(1, 1000000):

    result = run_collatz(x)
    counter = 1

    while result != 1:
        result = run_collatz(result)
        counter += 1
    
    if counter > MAX_CHAIN[1]:
        MAX_CHAIN[0] = x
        MAX_CHAIN[1] = counter


print MAX_CHAIN

