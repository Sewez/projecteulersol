import math

sum = 0

for x in range(1000):
    #print (x)
    if x % 3 == 0 or x % 5 == 0:
        sum = sum + x

print (sum)

def numrange(stop):
    i = 2
    while i < stop: 
        yield i
        i += 1

def isprim(num): 
    if num < 2: 
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

# Extract list of prime numbers
prims = []

for x in numrange(600):
    if isprim(x): 
        prims.append(x)

print (prims)

# Get prim factors
def getfactors(num, list):
    for i in list[::-1]:
        if num % i == 0:
            return i

print (getfactors(1174, prims))