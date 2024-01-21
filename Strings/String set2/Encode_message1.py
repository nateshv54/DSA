
'''
Encoded String:
input: aaaabbbccc
output:a4b3c3
'''



from os import *
from sys import *
from collections import *
from math import *

def encode(message):
    # Write your code here.
    s=''
    char=message[0]
    count=1

    for i in range(1,len(message)):
        if message[i]==char:
            count+=1
        else:
            s+=char+str(count)
            char=message[i]
            count=1
    s+=char+str(count)

    return s

if __name__=="__main__":
    str1=input()
    print(encode(str1))