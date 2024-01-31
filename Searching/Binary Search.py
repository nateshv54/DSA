def binary_search(arr,l,h,key):
    if l<=h:
        mid=(l+h)//2

        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            return binary_search(arr,mid+1,h,key)
        else:
            return binary_search(arr,l,mid-1,key)
    else:
        return "Element not found"
arr=[1,2,3,10,50]
print(binary_search(arr,0,len(arr)-1,50))

#Note:We should use sorted array for binary_search


