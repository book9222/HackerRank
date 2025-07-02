#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # print(s[-2:])
    # print(s[:2], s[2:8])
    if s[-2:] == 'PM':
        if int(s[:2]) < 12:
            return str(int(s[:2])+12)+s[2:8]
        else: 
            return s[:8]
    if s[-2:] == 'AM':
        if int(s[:2]) >= 12:
            return str(int(s[:2])-12).zfill(2)+s[2:8] # zfill -> zero fill function
        else:
            return s[:8]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
