'''Minimum parenthesis
((()))....valid string
)()())))...invalid string
Return no.of parenthesis required for invalid string to become valid'''
from os import *
from sys import *
from collections import *
from math import *

def minimumParentheses(pattern):

    balance = 0  # Initialize a variable to keep track of the balance of parentheses.

    open_extra = 0  # Initialize a variable to count the extra open parentheses needed.

    for c in pattern:
        if c == "(":
            balance += 1  # Increment balance when an open parenthesis is encountered.
        elif c == ")":
            balance -= 1  # Decrement balance when a close parenthesis is encountered.
            
        if balance < 0:
            open_extra += 1  # If balance goes negative, it means an extra open parenthesis is needed.
            balance = 0  # Reset balance to 0 because we are considering the extra open parenthesis.

    extra_close = balance  # Any remaining balance represents extra close parentheses needed.

    return extra_close + open_extra  # Total extra parentheses needed is the sum of extra open and extra close parentheses.


if __name__=="__main__":
    str=input()
    print(minimumParentheses(str))
