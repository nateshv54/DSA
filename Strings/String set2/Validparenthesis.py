'''Minimum parenthesis
((()))....valid string
)()())))...invalid string
Return no.of parenthesis required for invalid string to become valid'''
from os import *
from sys import *
from collections import *
from math import *

def minimumParentheses(pattern):

    # Write your code here
    # Return the minimum number of parentheses required.
    balance=0
    open_extra=0
    for char in pattern:
        if char=="(":
            balance+=1
        elif char==')':
            balance-=1
        
        if balance<0:
            open_extra+=1
            balance=0
    extra_close=balance

    return extra_close+open_extra

if __name__=="__main__":
    str=input()
    print(minimumParentheses(str))