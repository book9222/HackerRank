#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    bird_set = set(arr)
    bird_dict = dict.fromkeys(bird_set, 0)
    for i in arr:
        bird_dict[i] += 1
    print(bird_dict)
    max_bird = max(bird_dict, key=bird_dict.get)
    print(max_bird)
    return max_bird

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
