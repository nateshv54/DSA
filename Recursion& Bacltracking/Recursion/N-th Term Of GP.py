'''
Problem statement
You are given the first term (A), the common ratio (R) and an integer N. Your task is to find the Nth term of the GP series.

The general form of a GP(Geometric Progression) series is A, A(R), A(R^2), A*(R^3) and so on where A is the first term of GP series

Note :
As the answer can be large enough, return the answer modulo 10^9 + 7.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <= 10
1 <= N <= 10^8
0 <= A <= 50 
0 <= R <= 100

Time limit: 1 second
Sample input 1 :
1
5 3 2 
Sample output 1 :
48
Explanation :
For N=5, A=3, and R=2. The GP series will be 3, 6, 12, 24, 48, and so on. Thus, the 5th term will be 48.  
Sample input 2 :
2
4 1 2
6 2 1 
Sample output 2 :
8
2'''


import sys
from sys import stdin

def nthTermOfGP(n, a, r):

    
    #Write your code here
    MOD = 10**9 + 7
    return (a * pow(r, n-1, MOD)) % MOD


t = int(sys.stdin.readline().strip())

while(t > 0):
    
    n, a, r = map(int,input().split())
    print(nthTermOfGP(n,a,r))
    t = t - 1
    