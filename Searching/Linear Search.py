def linearsearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return "Element Not Found"
    
        
arr=[3,5,8,2,9,10]
print(linearsearch(arr,9))