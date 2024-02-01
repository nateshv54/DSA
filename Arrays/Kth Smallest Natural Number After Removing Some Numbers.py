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
