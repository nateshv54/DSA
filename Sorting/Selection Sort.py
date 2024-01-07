def selection_sort(arr):
    for i in range(len(arr)-1):
        min_inx=i
        for j in range(i+1,len(arr)):
            if arr[min_inx]>arr[j]:
                min_inx=j
        arr[min_inx],arr[i]=arr[i],arr[min_inx]
    print(arr)

arr=[1,5,3,4,8]
selection_sort(arr)