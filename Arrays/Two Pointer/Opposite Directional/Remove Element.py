def remove_target_element_2pointer(arr,target):
    start=0
    end=0

    while end<len(arr):
        if arr[end]!=target:
            arr[start]=arr[end]
            start+=1
        end+=1
    return arr

arr=[1,6,5,9,8]
print(remove_target_element_2pointer(arr,6))