'''
Problem statement
You are given a number 'N' in the form of a string 'S', your task is to find the smallest number strictly greater than the given number 'N' which is a palindrome.

Note:

1) A palindrome is a word, number, phrase, or another sequence of characters that reads the same backward as forward, such as 'naman', 'abcba', '1234321', etc
2) The numerical value of the given string 'S' will be greater than 0.
3) A single-digit number is also considered as a palindrome.
4) Note that the length of the string 'S' is nothing but the number of digits in the number 'N'.
Sample Input 1:
1
4
1221
Sample Output 1:
1331
Explanation for sample input 1:
The next smaller palindrome to 1221 is 1331, as it is strictly greater than 1221 and it reads the same from the front and back both.
Sample Input 2:
1
3
999
Sample Output 2:
1001
Explanation for sample input 1:
The next smaller palindrome to 999 is 1001, as it is strictly greater than 999 and it reads the same from the front and back both.'''

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)

def nextLargestPalindrome(s, length):
    carry = 1
    lst = list(s)
    # Loop to add 1 to the number.
    for i in range(length - 1, -1, -1):
        digit = int(lst[i])
        if digit + carry <= 9:
            lst[i] = chr(digit + carry + 48)
            carry = 0

        else:
            temp = (int(lst[i]) + carry) % 10
            lst[i] = chr(temp + 48)
            carry = 1

    s = ''.join(lst)
    if carry:
        s = "1" + s

    i, j = 0, len(s) - 1
    pos = -1
    conditionViolated = False
    s = list(s)
    while i <= j:
        if s[i] < s[j]:
            s[j] = s[i]
            pos = i
            conditionViolated = True

        elif s[i] > s[j]:
            s[j] = s[i]
            conditionViolated = False

        elif conditionViolated and s[i] != '9':
            pos = i

        i += 1
        j -= 1
    # Checking if the condition is violated or not.
    # Finding the smallest palindrome strictly greater than the input number.
    if conditionViolated:
        s[pos] = chr(int(s[pos]) + 1 + 48)
        s[len(s) - 1 - pos] = s[pos]
        for i in range(pos + 1, (len(s) - 1) // 2 + 1):
            s[len(s) - 1 - i] = s[i] = '0'

    return ''.join(s)

# Taking input using fast I/0
def takeInput():
    N = int(stdin.readline())
    S = stdin.readline().strip()
    return N, S

tc = int(input())
while tc > 0:
    N, S = takeInput()
    S = nextLargestPalindrome(S, N)
    stdout.write(S + "\n")
    tc -= 1
