#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    bill_anna = bill.copy()
    bill_anna.pop(k)
    anna_con  = sum(bill_anna)/2
    sum_con = sum(bill)/2
    if anna_con == b :
        print('Bon Appetit')
    elif anna_con < b :
        print(int(sum_con - anna_con))
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
