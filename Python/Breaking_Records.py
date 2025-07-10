#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    break_min = 0
    break_max = 0
    min_score = scores[0]
    max_score = scores[0]
    
    for i in scores:
        print(i, min_score, max_score, break_min, break_max)
        if i > max_score:
            break_max += 1
            max_score = i
        if i < min_score:
            break_min += 1
            min_score = i
        
    return [break_max, break_min]
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
