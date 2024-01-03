def insertion_sort(arr):
    for i in range(len(arr)):
        k=arr[i]
        j=i-1
        while(j>=0 and arr[j]>k):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=k
    print(arr)

arr=[2,5,6,3,1]
insertion_sort(arr)