'''
    Time Complexity : O(N)
    Space complexity : O(1)

    where N is the size of the input array



    You have been given an integer array/list (ARR) of size N. You have to return an array/list PRODUCT such that PRODUCT[i] is equal to the product of all the elements of ARR except ARR[i]

 Note :
Each product can cross the integer limits, so we should take modulo of the operation. 

Take MOD = 10^9 + 7 to always stay in the limits.
Follow up :
Can you try solving the problem in O(1) space?
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <= 100
0 <= N <= 10^5
0 <= ARR[i] <= 10^5

Time Limit: 1 sec
Sample Input 1 :
2
3
1 2 3
3
5 2 2
Sample Output 1 :
6 3 2
4 10 10
Explanation for Sample Output 1 :
 Test case 1 : Given array = {1, 2, 3] 
 Required array = [2 * 3, 1 * 3, 1 * 2] = [6, 3, 2]
 Test case 2 : Given array = {5, 2, 2] 
 Required array = [2 * 2, 5 * 2, 5 * 2] = [4, 10, 10]
Sample Input 2 :
2
1
100
2
1 2
Sample Output 2 :
1
2 1
'''
from sys import stdin
mod = 10 ** 9 + 7
def getProductArrayExceptSelf(arr, n) :
    output = [1] * n
    product = 1
    for i in range(n) :
        
        output[i] = product
        product = (product * arr[i]) % mod
    
    product = 1
    for i in range(n - 1, -1, -1) :
        
        output[i] =(output[i] * product) % mod
        product = (product * arr[i]) % mod

    return output

def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n

def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ") 
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    product = getProductArrayExceptSelf(arr, n)
    printList(product, n)
    
    t -= 1