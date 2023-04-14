#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getPrefixScores' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getPrefixScores(arr):
    # Write your code here
    ans = []
    prev_max, curr_max = 0, 0
    
    for i in arr:
        curr_max += i
        ans.append(prev_max + curr_max)
        prev_max = ans[-1] 
        
    curr_max = 0
    for i in range(len(arr)):
        curr_max = max(curr_max, arr[i])
        ans[i] += (i+1)*curr_max
        ans[i] %= (10**9+7)
        
        
    return ans
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getPrefixScores(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
