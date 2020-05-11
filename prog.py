#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s="".join(s.split(" "))
    newlist,j=[],0
    print(len(s))
    rows=math.floor(math.sqrt(len(s)))
    cols=math.ceil(math.sqrt(len(s)))
    if rows*cols<len(s):
        rows+=1
    for i in range(rows):
        if j+cols<len(s):
            newlist.append(s[j:j+cols])
        else:
            newlist.append(s[j:len(s)])
        j+=cols
    newlist1=[]
    for j in range(cols):
        string=""
        for i in range(rows-1):
            string+=newlist[i][j]
        newlist1.append(string)
    lastline=""
    for i in range(len(newlist[rows-1])):
        newlist1[i]+=newlist[rows-1][i]
    return " ".join(newlist1)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

