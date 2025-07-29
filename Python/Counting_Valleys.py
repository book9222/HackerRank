#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valley = 0
    h = 1
    trail = "-"
    con_d = 0
    for i in path:
        if i == "U":
            trail += "/"
            h += 1
        elif i == "D":
            trail += "\\"
            h -= 1
        if h < 1 and i == "D":
            con_d += 1
        elif h >= 1 and i == "U" and con_d >= 1:
            valley += 1
            con_d = 0
            
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
