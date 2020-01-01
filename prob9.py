# Problem >> https://projecteuler.net/problem=9

def check_triplet(x, y, z): 
    if ((x*x) + (y*y)) == (z*z): 
        if (x < y < z):
            return True
    else:
        return False




def run_test():
    #Initialize x with 1
    x = 1

    while x < 501: 
        # loop y through a range of x to half the range of x:1000
        for y in range (x, 1000): 

            # z will always take the remaining space withing the 1000 range (not taken by x or y while maintaining the size order)
            z = 1000 - x - y
            
            # exit loop if y has exceeded the half range of x : 1000 (no way Z would still be larger than y in this case)
            if y >= z:
                break
            
            if check_triplet(x, y, z):
                print (x, y, z)
                return True
        
        # if the check failed, increase initial x value by 1 and try again
        x = x + 1
    
    return False

# Run the test to search for the triple
print run_test()
