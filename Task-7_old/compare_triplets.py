import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    a_score=0
    b_score=0
    scr=[]
    for i in range(3):
        if a[i]>b[i]:
            a_score=a_score+1
        elif a[i]<b[i]:
            b_score=b_score+1    
    scr.insert(0,a_score)
    scr.insert(1,b_score)
    return scr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
