def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

arr=[1,3,2,4,10,12]
print("sorted array is",bubble_sort(arr))