def product_sub_arr(arr):
    curr_prod=1
    max_prod=1
    for i in range(0,len(arr)):
        curr_prod*=arr[i]
        max_prod=max(max_prod,curr_prod)

        if curr_prod==0:
            curr_prod=1
    return max_prod

arr=[6,-3,-10,0,2]
arr1=[-1,-3,-10,0,60]
arr2=[-1,-3,-4]
print(product_sub_arr(arr2))