'''
    Time Complexity: O(N * log(N))
    Space Complexity: O(log N)

    Where 'N' is the number of elements in the given array/list.
'''

# Function to partition the array using Dutch National Flag algorithm
def partition(arr, l, h, start, mid):
    pivot = arr[h]  # Choosing the pivot element as the last element
    end = h
    
    # Iterate while mid is not greater than end.
    while (mid[0] <= end):
        # Place the element at the starting if it's value is less than pivot.
        if arr[mid[0]] < pivot:
            arr[mid[0]], arr[start[0]] = arr[start[0]], arr[mid[0]]
            mid[0] = mid[0] + 1
            start[0] = start[0] + 1
        # Place the element at the end if it's value is greater than pivot.
        elif arr[mid[0]] > pivot:
            arr[mid[0]], arr[end] = arr[end], arr[mid[0]]
            end = end - 1
        else:
            mid[0] = mid[0] + 1

# Recursive function to perform quicksort using Dutch National Flag algorithm
def quicksort(arr, l, h):
    # Base case when the size of the array is 1.
    if l >= h:
        return
    
    # To handle the case when there are only 2 elements in the array.
    if h == l + 1:
        if arr[l] > arr[h]:
            arr[l], arr[h] = arr[h], arr[l]
            return
    
    start = [l]
    mid = [l]
    
    # Function to partition the array.
    partition(arr, l, h, start, mid)
    
    # Recursively sort the left and the right partitions.
    quicksort(arr, l, start[0] - 1)
    quicksort(arr, mid[0], h)

# Main function to sort the array using Dutch National Flag algorithm
def quickSortUsingDutchNationalFlag(arr):
    # Call the quicksort function.
    quicksort(arr, 0, len(arr) - 1)
    
    # Return the array/list after sorting.
    return arr

# Driver code to test the quickSortUsingDutchNationalFlag function
if __name__ == "__main__":
    # Test Case
    arr = [4, 2, 1, 4, 2]
    print("Original array:", arr)
    result = quickSortUsingDutchNationalFlag(arr)
    print("Sorted array:", result)

    arr = [14, 8, 10, 7, 6]
    print("Original array:", arr)
    result = quickSortUsingDutchNationalFlag(arr)
    print("Sorted array:", result)
