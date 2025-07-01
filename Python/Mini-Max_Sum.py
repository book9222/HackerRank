#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    ans=[]
    for i in range(len(arr)):
        tmp = arr.copy()
        tmp.pop(i)
        # print(sum(tmp))
        ans.append(sum(tmp))
    print(min(ans), max(ans))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
