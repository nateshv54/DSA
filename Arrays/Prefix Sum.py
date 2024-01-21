def prefix_sum(arr):
    sum=0
    for i in range(0,len(arr)):
        arr[i]+=sum
        sum=arr[i]
    return arr
arr=[1,2,3,4,5,6]
prefix_sum(arr)
print("Sum of array from 2 to 5 is")
print(arr)
print(arr[5]-arr[2-1])