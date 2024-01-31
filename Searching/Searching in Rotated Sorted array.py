#Technique: Modified Binary Search
def search_in_rotated_array(arr, key):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        # Check if the left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= key <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # If the left half is not sorted, the right half must be sorted
        else:
            if arr[mid] <= key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

# Input reading and processing
N = int(input())
arr = list(map(int, input().split()))
Q = int(input())

# Process each query
for _ in range(Q):
    key = int(input())
    result = search_in_rotated_array(arr, key)
    print(result)
