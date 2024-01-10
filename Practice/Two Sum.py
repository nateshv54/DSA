def two_sum(arr, target):
    result = []
    start = 0
    end = len(arr) - 1
    
    # Sort the array before applying the two-pointer technique
    arr.sort()
    
    while start < end:
        current_sum = arr[start] + arr[end]
        
        if current_sum == target:
            result.append((arr[start], arr[end]))
            start += 1
            end -= 1
        elif current_sum < target:
            # Increment the left pointer value
            start += 1
        else:
            # Decrease the right pointer value
            end -= 1
    
    # If no pairs are found or the array has only one element, append (-1, -1)
    if not result or len(arr) == 1:
        result.append((-1, -1))
    
    return result


arr=[1,5,8,9,10,0]
print(two_sum(arr,1))

'''
O(n)
Technique Used:
 Two pointer technique in opposite direction
 It is always better to sort the elements before applying two pointer technique
'''