# Given an array of N non-negative integers arr[] representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# Examples:  

# Input: arr[] = {2, 0, 2}
# Output: 2
# Explanation: The structure is like below.
# We can trap 2 units of water in the middle gap.

def max_water(arr):
    # initializing indexes to traverse array
    start,end=0,len(arr)-1

    #To store left_max and right_max for two pointers for start,end
    l_max,r_max=0,0

    #To store final result
    result=0

    while(start<=end):
        #check for min(left,right) for each element
        r_max=max(r_max,arr[end])
        l_max=max(l_max,arr[start])
        
        if r_max<=l_max:
            result+=max(0,r_max-arr[end])
            #Update right max

            end-=1
        else:
            result+=max(0,l_max-arr[start])
            #update left_max
            start+=1

    return result

arr=[0,1,0,2,1,0,1,3,2,1,2,1]
print(max_water(arr))
