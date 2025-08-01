#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    sock_dict = {}
    for i in ar:
        print(sock_dict)
        if i not in sock_dict.keys():
            sock_dict[i] = 1
        elif sock_dict[i] == 1:
            sock_dict[i] -= 1
            pairs += 1
        elif sock_dict[i] == 0:
            sock_dict[i] += 1
    print(pairs)
    return(pairs)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
