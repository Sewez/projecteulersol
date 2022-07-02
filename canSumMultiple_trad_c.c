/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#define TOTAL_TRIALS_FOR_8_BITS 255
#define TRUE 1
#define FALSE 0

typedef unsigned char UINT8;
typedef unsigned int UINT32;

UINT32 arrToSearch[] = {0, 0, 0, 0, 0, 0, 3, 3};

static UINT8 canSum(UINT32 m, UINT32 * arr);

UINT8 canSum(UINT32 m, UINT32 * elem) {
    // test print sum of the array 
    UINT8 b_array_counter = 0; 
    UINT32 sum = m;
    
    
    while (b_array_counter < TOTAL_TRIALS_FOR_8_BITS) {
        b_array_counter++;
        
        for (int i = 0; i < sizeof(b_array_counter) * 8; i++) {
            // Binary counter for scanning
            UINT8 temp_binary = (b_array_counter & (1 << i)) >> i;
            //printf("%d", temp_binary);
            
            // Sum array elements that matches the binary counter used for scanning
            if (temp_binary != 0) {
                sum -= elem[i];
                int temp_sum = (int)sum;
                
                // Loop to check if multiples of the current element can achieve zero
                if (elem[i] > 0 ) {
                    while (temp_sum > 0) {
                        temp_sum -= elem[i];
                    }
                    
                    if (temp_sum == 0) {
                        return TRUE;
                    }
                }
                
            }
        }
        
        if (sum == 0) {
            return TRUE;
        }
        
        // Reset sum for next iternation
        sum = m;
    }
    
    // Sum of input elements doens't match the seed, retrun False
    return FALSE;
}

int main()
{
    UINT8 retValue = canSum(8, arrToSearch);
    printf("%d", retValue);

    return 0;
}

