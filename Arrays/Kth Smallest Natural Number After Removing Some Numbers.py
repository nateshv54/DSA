'''
You have a list of all-natural numbers and an ‘arr’. Your task is to find the Kth smallest natural number after removing all numbers in ‘arr’ from the list of all-natural numbers.

Note: ‘arr’ will be sorted in ascending order.

For example:
You are given, ‘arr’ = [1, 2, 4], ‘K’ = ‘5’, You have the natural numbers as [1, 2, 3, 4, 5, 6, 7 .. ], after removing all the integers in the array from natural numbers, we have, [3, 5, 6, 7, 8]. Here 8 is the 5th smallest number. Hence the answer is 8.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= N <= 10^3
1 <= K <= 10^6
1 <= arr[i] <= 10^5

Time Limit: 1 sec.
Sample Input 1:
2
3 5
1 2 4
4 5
1 2 4 5
Sample Output 1:
8
9
Explanation:
For the first test case,‘arr’ = [1, 2, 4], ‘K’ = ‘5’, You have the natural numbers as [1, 2, 3, 4, 5, 6, 7 .. ], after removing all the integers in the array from natural numbers, we have, [3, 5, 6, 7, 8]. Here 8 is the 5th smallest number. Hence the answer is 8.

For the second test case,‘arr’ = [1, 2, 4, 5], ‘K’ = ‘5’, You have the natural numbers as [1, 2, 3, 4, 5, 6, 7 .. ], after removing all the integers in the array from natural numbers, we have, [3, 6, 7, 8, 9]. Here 9 is the 5th smallest number. Hence the answer is 9.
Sample Input 2:
2
1 5
5
3 3
2 3 4
Sample Output 2:
6
6'''
from typing import List

def kthSmallest(arr: List[int], k: int) -> int:
    markedNums = set()
    MAX = 1000000

    # Mark all the numbers in the arr.
    for num in arr:
        markedNums.add(num)

    i = 1
    while i <= MAX:
        # If the number is not marked then we can decrease k.
        if i not in markedNums:
            k -= 1

        # If k is 0 return i.
        if k == 0:
            return i

        i += 1

    # This code is not reachable.
    return -1

# Example usage with user input
T = int(input("Enter the number of test cases: "))
for _ in range(T):
    N, K = map(int, input("Enter the size of arr and k separated by space: ").split())
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))

    result = kthSmallest(arr, K)
    print(result)
