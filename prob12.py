# Problem 12 >> https://projecteuler.net/problem=12

def number_of_factors(num):
    counter = 0
    for x in range (1, num): 
        if num % x == 0: 
            counter += 1
    
    return counter


# Caculate triangular
MAX_VALUE = 1000000000
triang = 0

for i in range(1, MAX_VALUE): 
    triang += i

    if number_of_factors(triang) == 50:
        print triang
        break
