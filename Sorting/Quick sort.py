def quicksort(arr,low,high):
    if low<high:
        #partition array around pivot element
        pivot_index=partition(arr,low,high)

        #now apply recursion for two partitions
        quicksort(arr,low,pivot_index-1)
        quicksort(arr,pivot_index+1,high)
    return arr



def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]

    #Move the pivot element to end of list
    arr[i+1],arr[high]=arr[high],arr[i+1]
    #return pivot index
    return i+1


arr=[2,3,5,6,9,8,1]
print(quicksort(arr,0,len(arr)-1))
