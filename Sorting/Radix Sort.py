
def counting_sort(arr,place):
    n=len(arr)
    output=[0]*n

    count=[0]*10
    #count the occurance
    for i in range(0,n):
        index=arr[i]//place
        count[index%10]+=1
    #update count array
    for i in range(1,10):
        count[i]+=count[i-1]

    #Build the output array
    i=n-1
    while i>=0:
        index=arr[i]//place
        output[count[index%10]-1]=arr[i]
        count[index%10]-=1
        i-=1

    #copy elements from one array to another
    for j in range(0,len(arr)):
        arr[j]=output[j]

def radix_sort(arr):
    max1=max(arr)

    #digits place
    place=1
    while max1//place >0:
        counting_sort(arr,place)
        place*=10
    return arr


arr=[175,45,70,2,24,36,99]
print(radix_sort(arr))