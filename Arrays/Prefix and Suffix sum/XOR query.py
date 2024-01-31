'''
You're given an initially empty array. You perform queries of two types:

    Add a value to the end of the array.
    Perform bitwise XOR on all elements in the array with a given value.

The task is to return the array after executing all queries. The provided code uses a cumulative XOR array to efficiently compute the final array state after multiple XOR operations.'''


def xorQuery(queries):
    ans = []
    xorArray = [0] * (10**5 + 1)
    
    for i in range(len(queries)):
        if queries[i][0] == 1:
            ans.append(queries[i][1])
        else:
            xorArray[0] ^= queries[i][1]
            xorArray[len(ans)] ^= queries[i][1]

    for i in range(len(ans)):
        if i == 0:
            ans[i] = ans[i] ^ xorArray[i]
        else:
            xorArray[i] ^= xorArray[i - 1]
            ans[i] ^= xorArray[i]

    return ans

# Example Usage:
queries = [(1, 2), (1, 3), (2, 4)]
result = xorQuery(queries)
print(result)

'''
Explanation:

    Create an empty list ans to store the answers.

    Create an array xorArray of size 10^5 + 1 initialized with zeros. This array will be used to keep track of the XOR values for each position in the array.

    Iterate over all the queries:
        For Type 1 queries, append the value to the ans list.
        For Type 2 queries, update the xorArray to store XOR values at the beginning and end of the array.

    Compute the cumulative prefix XOR and evaluate the final answer:
        Iterate over the length of the ans list.
        If the index is 0, the answer at that index is XOR-ed with the corresponding xorArray value.
        For subsequent indices, update the xorArray value and XOR it with the current element in ans.

    Return the final ans list.'''