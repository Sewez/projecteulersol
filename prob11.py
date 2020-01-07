# Problem 11 >> https://projecteuler.net/problem=11
import random
import itertools

def gen_random_grid(size): 
    return [[random.randint(1, 99) for i in range(size)] for x in range(size)]

def base_scan(grid):
    x = 0 
    y = 0 

    multiple_size = 4
    # [Max, x_location, y_location, scan_type]
    max_multi_found = [1, 1, 1, "N/A"]
    multi = 1

    while x < len(grid):
        while y < len(grid[x]): 
            #  print('{0:{width}}'.format(grid[x][y], width=5)),

            # Run your check
            # Horizontal Scan
            if (y + multiple_size) <= (len(grid[x])):
                for num in range(multiple_size):
                    multi = multi * grid[x][y+num]

                if multi > max_multi_found[0]: 
                    max_multi_found = [multi, x, y, "Horizontal"]
                
                multi = 1

            # Vertical Scan
            if (x + multiple_size) <= (len(grid)):
                for num in range(multiple_size):
                    multi = multi * grid[x+num][y]

                if multi > max_multi_found[0]: 
                    max_multi_found = [multi, x, y, "Vertical"]
                
                multi = 1
            # Diagonal Plus
            # boundary check
            if (x + multiple_size) <= (len(grid)) and (y + multiple_size) <= (len(grid[x])):
                for num in range(multiple_size):
                    multi = multi * grid[x+num][y+num]

                if multi > max_multi_found[0]: 
                    max_multi_found = [multi, x, y, "Diagonal Plus"]
                
                multi = 1
            # Diagonal Minus 
            if (x + multiple_size) <= (len(grid)) and (y - multiple_size + 1) >= (0):
                for num in range(multiple_size):
                    multi = multi * grid[x+num][y-num]

                if multi > max_multi_found[0]: 
                    max_multi_found = [multi, x, y, "Diagonal Minus"]
                
                multi = 1

            y = y + 1
        #  print '\n',
        x = x + 1
        y = 0

    print ("The maximum found multi of {0} is {1} \n at locations {2}/{3} with {4} Scan".format(multiple_size, \
    max_multi_found[0], max_multi_found[1], max_multi_found[2], max_multi_found[3]))

test_grid = gen_random_grid(20)
# test_grid = [[96,49,26], [9,58,55], [23,54,7]]
base_scan(test_grid)

# # Print grid for test
for x in test_grid:
    for y in x: 
        print('{0:{width}}'.format(y, width=5)),
    print

