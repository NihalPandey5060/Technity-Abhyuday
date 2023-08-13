import math
import os
import random
import re
import sys

def timeConversion(s):
    t = s.split(":")
    if s[-2:] == "PM":
        if t[0] != "12":
            t[0] = str(int(t[0])+12)
    else:
        if t[0] == "12":
            t[0] = "00"
    nt = ':'.join(t)
    return str(nt[:-2])   

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
