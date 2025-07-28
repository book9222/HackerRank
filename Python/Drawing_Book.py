#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    book_dict = {'l': [i for i in range(0,n+1,2)], 'r': [i for i in range(1,n+1,2)]}
    # print(book_dict)
    if p in book_dict['l']:
        i = book_dict['l'].index(p)
        # print(book_dict['l'],i)
    elif p in book_dict['r']:
        i = book_dict['r'].index(p)
        # print(book_dict['r'],i)
    return min(i, len(book_dict['l'])-1-i)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
