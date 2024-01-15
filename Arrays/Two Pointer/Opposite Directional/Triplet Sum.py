def triplet_sum(arr,target):
    #sort arr for better results while using 2 pointer
    arr.sort()
    for i in range(0,len(arr)-2):
        #we run loop until len(arr)-2,bcz l runs until len(arr)-1
        l=i+1
        #pointer for last element
        r=len(arr)-1

        while(l<r):
            if(arr[i]+arr[l]+arr[r]==target):
                print("Triplet is ",arr[i],arr[l],arr[r])
                return True
            elif ((arr[i]+arr[l]+arr[r])<target):
                l+=1
            else:   #arr[i]+arr[l]+arr[r]>sum
                r-=1
        
    return False
    
arr=[1, 4, 45, 6, 10, 8]
target=22
triplet_sum(arr,target)
