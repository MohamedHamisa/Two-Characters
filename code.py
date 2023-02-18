#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    s_char = sorted(list(set(s)))
    s_check = []
    res = 0
    
    for i in range(len(s_char)-1):
        for j in range(i+1,len(s_char)):
            s_check.append([s_char[i],s_char[j]])
    
    for i in s_check:
        s_tmp = []
        
        for j in s:
            if j == i[0] or j == i[1]:
                s_tmp.append(j)
        
        compare = 0
        res_tmp = 0
        for j in s_tmp:
            if j != compare:
                res_tmp += 1
                compare = j
            else:
                res_tmp = 0
                break
        if res_tmp > res:
            res = res_tmp
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
