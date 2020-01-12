# Problem 12 >> https://projecteuler.net/problem=12

def number_of_factors(num):
    counter = 0
    max_range = num

    for x in range (1, num): 
        if num % x == 0: 
            # New max range for the check is now the reulst of this division
            max_range = num / x

            if (x >= max_range):
                break

            # Both the divide number and result are factors of num, hence add 2
            counter += 2

            # print (x)
            # print (max_range)

    return counter


# Caculate triangular
MAX_VALUE = 1000000000
triang = 0

for i in range(1, 10000000): 
    triang += i

    if number_of_factors(triang) >= 500:
        print triang
        break

# print number_of_factors(55)