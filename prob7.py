
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prim(num):
    for x in range(2, num-1):
        if num % x == 0: 
            return False
        
    # Number is prim
    return True


# for x in range (2, 100): 
x = 2
counter = 0
while True:
    if is_prim(x):
        counter += 1

        if counter == 6:
            print x
            # 13
        elif counter == 10001: 
            print x
            # 104743
            break
    x += 1
