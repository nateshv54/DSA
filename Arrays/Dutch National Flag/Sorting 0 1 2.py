def sort012(arr, n):
    # l, mid, and h represent the pointers for 0s, 1s, and 2s respectively
    l = 0
    mid = 0
    h = n - 1
    
    # Traverse the array until mid crosses high
    while mid <= h:
        # If the current element is 0, swap it with the element at 'l' and move both 'l' and 'mid' pointers ahead
        if arr[mid] == 0:
            arr[mid], arr[l] = arr[l], arr[mid]
            mid += 1
            l += 1
        # If the current element is 2, swap it with the element at 'h' and move 'h' pointer backward
        elif arr[mid] == 2:
            arr[mid], arr[h] = arr[h], arr[mid]
            h -= 1
        # If the current element is 1, move 'mid' pointer ahead
        else:
            mid += 1

# Driver Code
arr = [1, 0, 2, 1, 0, 1, 2, 0, 1, 2, 1, 1, 0, 0, 2, 2, 1, 0, 2, 1]
n = len(arr)

print("Original Array:", arr)
sort012(arr, n)
print("Sorted Array:", arr)
