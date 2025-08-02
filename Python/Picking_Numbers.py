#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    array_count = 1
    for i in range(len(a)-1):
        # print(a[i],a[i+1],abs(a[i]-a[i+1]))
        if abs(a[i]-a[i+1]) <= 1:
            array_count += 1
        else: 
            pass
        # print()
    return array_count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
