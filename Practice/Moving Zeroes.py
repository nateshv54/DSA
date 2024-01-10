def moveZeros( a: [int]) -> [int]:
    # Write your code here.
    left=0
    right=0
    while right<len(a):
        if a[right]!=0:
            a[left],a[right]=a[right],a[left]
            left+=1
        right+=1
    return a

a =[0,3,0,6,7,0]
print(moveZeros(a))

'''
O(n)

Two pointer technique with same direction
    -Both pointer start at same point 0
    -left pointer is to keep track of non-zero elements
    -right pointer is to traverse the array elements
    ->If element is zero,swap values with non-zero values and increment
       left pointer
     -else 
       increment right pointer'''