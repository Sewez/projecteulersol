# URL > https://projecteuler.net/problem=10

def is_prim(num):
    for x in range(2, num-1):
        if num % x == 0: 
            return False
        
    # Number is prim
    return True

sum = 0 

for x in range(2, 200000): 
    if is_prim(x): 
        sum = sum + x

print sum
