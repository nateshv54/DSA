def merge_sort(arr):
    if len(arr)<=1:
        return  arr
    mid=len(arr)//2
    #divide the array into two halves
    left_half=arr[:mid]
    right_half=arr[mid:]
    
    #Recursively sort the both 
    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)

    #combine the both halves
    i=j=k=0
    while i<len(left_half) and j<len(right_half):
        if left_half[i]<right_half[j]:
            arr[k]=left_half[i]
            i+=1
        else:
            arr[k]=right_half[j]
            j+=1
        k+=1

    #add the remaing elements of left_half
    while i<len(left_half):
        arr[k]=left_half[i]
        i+=1
        k+=1
    
    #add the remaining elements of right_half
    while j<len(right_half):
        arr[k]=right_half[j]
        j+=1
        k+=1

    return arr

arr=[9,3,6,5,7,8,10,11]
print("Sorted Merge array ",merge_sort(arr))