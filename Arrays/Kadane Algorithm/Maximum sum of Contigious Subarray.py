def maxSum_of_Contigious_subarray(arr):
    curr_sum=0
    #initialize max_sum to min value,denotes empty subarray
    max_sum=float('-inf')
    for i in range(0,len(arr)):
        curr_sum=curr_sum+arr[i]
        
        max_sum=max(curr_sum,max_sum)
        #checking if curr_sum becomes negative
        if curr_sum<0:
            curr_sum=0
   

    return max_sum

arr=[1,2,-5,8,-3,-5,3,4]
print(maxSum_of_Contigious_subarray(arr))


'''Note: In cpp the exact value of INT_MIN is -2147483648. This value represents the smallest 
    (most negative) representable value for a 32-bit signed integer
     In python there is no concept of 32bit signed interger, float('-inf') in python servers same purpose of INT_MIN in cpp '''
    