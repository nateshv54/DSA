def Rot_count_rSorted_arr(arr):
    min_index=0
    for i in range(1,len(arr)):
        if arr[i]<arr[min_index]:
            min_index=i
    return min_index

arr=[5,6,1,2,4]
print(Rot_count_rSorted_arr(arr))

#Note: Try to implement function returns rotated array

      