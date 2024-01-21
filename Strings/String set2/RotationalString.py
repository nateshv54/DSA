'''
Left and Right Rotational String

'''
from os import *
from sys import *
from collections import *
from math import *

def leftRotate(strr, d):    
    # Write your code here.
    if d <= len(strr):
        return strr[d:] + strr[:d]
    else:
        return leftRotate(strr, d%len(strr))
def rightRotate(strr, d):    
    # Write your code here.
    if d <= len(strr):
        return  strr[len(strr)-d: ] + strr[:len(strr)-d]
    else:
        return rightRotate(strr, d%len(strr))

'''
#include <bits/stdc++.h> 
string leftRotate(string str, int d) {
    // Write your code here.
    string s1=str.substr(0,d);
    string s2=str.substr(d);
    return s2+s1;
}

string rightRotate(string str, int d) {
    // Write your code here.
    string s1=str.substr(0,str.length()-d);
    string s2=str.substr(str.length()-d);
    return s2+s1;
}'''