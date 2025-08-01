#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    ans = 0
    
    for i in range(max(a), min(b)+1):
        # print("i", i)
        between_sets = True
        for j in a: # Check if i is a multiple of all elements in a if not break
            if i % j != 0:
                # print("j--->", j)
                between_sets = False
                break
        for j in b: # Check if all elements in b are multiples of i if not break
            if j % i != 0:
                between_sets = False
                break
        if between_sets :
            ans += 1
    
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
