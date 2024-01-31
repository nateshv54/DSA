
'''
Problem Statement:

You are given an array A of length N, and you have also defined a new array B as the concatenation of array A for an infinite number of times.

For example, if the given array A is [1, 2, 3], then the infinite array B will be [1, 2, 3, 1, 2, 3, 1, 2, 3, ...].

Now, you are given Q queries, each query consisting of two integers L and R (1-based indexing). Your task is to find the sum of the subarray from index L to R (both inclusive) in the infinite array B for each query.

Write a function sumInRanges(arr, n, queries, q) to solve this problem. The function takes the following parameters:

    arr: An array of N integers (1 <= N <= 10^4), representing the given array A.
    n: An integer (1 <= n <= 10^9), representing the length of the given array A.
    queries: A list of Q tuples, where each tuple (L, R) represents a query (1 <= L, R <= 10^18).
    q: An integer (1 <= q <= 10^4), representing the number of queries.

The function should return a list of integers, where the ith element of the list is the sum of the subarray from index L to R (both inclusive) in the infinite array B for the ith query.

Ensure that the value of the sum is returned as modulus 10^9+7.'''

# Function to calculate prefix sum upto index x of the infinite array.
def func(sumArray, x, n):
    mod = 10 ** 9 + 7

    # Number of times the given array comes completely up to index x.
    count = (x // n) % mod
    res = (count * sumArray[n]) % mod

    # Adding the remaining elements sum.
    res = (res + sumArray[x % n]) % mod

    return res

def sumInRanges(arr, n, queries, q):
    mod = 10 ** 9 + 7

    # It stores answer for each query.
    ans = []

    # It stores cumulative sum where sumArray[i] = sum(A[0]+..A[i]).
    sumArray = [0 for i in range(n + 1)]

    for i in range(1, n + 1):
        sumArray[i] = (sumArray[i - 1] + arr[i - 1]) % mod

    # Traversing the given queries.
    for ranges in queries:
        l = ranges[0]
        r = ranges[1]

        # It stores the prefix sum from index 0 to index r in an infinite array.
        rsum = func(sumArray, r, n)

        # It stores the prefix sum from index 0 to index l-1 in an infinite array.
        lsum = func(sumArray, l - 1, n)

        # Add answer for each query.
        ans.append((rsum - lsum + mod) % mod)

    return ans



arr = [10, 4, 2, 5, 53, 5, 7]
n = 7
queries = [(1, 1), (7, 7), (3, 5), (1, 2), (2, 2), (11, 11), (1, 10), (12, 14, 53), (1, 7)]
q = 9

result = sumInRanges(arr, n, queries, q)
print(result)
