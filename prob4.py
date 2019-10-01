# Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.


# Function to check palindomic numbers
def check_palin(int_list):
    j = 0

    # Simple loops to compare the current value for it's mirror in the list
    for i, x in enumerate(int_list):
        if i == (len(int_list) - 1 - i):
            break

        if x == int_list[len(int_list) - 1 - i]:
            continue
        else: 
            return False
        

    # return T or F
    return True

# Breaks down a number into a list of it's digitsy
def breakdown_int(num): 
    i = 1
    y = []

    # extract matching factors
    while i <= num: 
        y.insert(0, i)
        i *= 10
    
    # extract division values
    div = [num / i for i in y]
    # create a copy to update with extractions from factors
    copy = [i for i in div]

    # loop and extract each number indvidually in a list
    for i, v in enumerate(div): 
        if i > 0:
            copy[i] = v - (div[i-1] * 10)
    
    return copy


def run_test(rev_list):
    for x in rev_list_gen: 
        for y in rev_list_gen: 
            check_list = breakdown_int(x * y)
            if check_palin(check_list):
                return x, y, x * y


# Creat reversed list of all 3 digit number
rev_list_gen = range(999,99, -1)
print run_test(rev_list_gen)
