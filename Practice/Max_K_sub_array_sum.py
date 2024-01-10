#Maximum sum of subarrays having distinct elements of length K
'''
Given an array, arr[] and a value k, represent the length of the subarray to be considered. 
Find the maximum sum that can be obtained from the subarray of length k such that each element of the subarray is unique.
 If there is no subarray that meets the required condition then return 0.'''

def max_sub_arraySum(arr,k):
    max_sum=0
    Window_sum=0
    for i in range(0,k):
        Window_sum+=arr[i]
    
    for j in range(k,len(arr)):
        Window_sum+=arr[j]-arr[j-k]
        max_sum=max(max_sum,Window_sum)
    return max_sum

arr=[1, 5, 4, 2, 9, 9, 9]
print("Maximum subarray sum is ",max_sub_arraySum(arr,3))