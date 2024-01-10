def remove_duplicates_sortedarray(arr):
    start = 0
    for i in range(1,len(arr)):
        if arr[i]!=arr[start]:
            start+=1
            arr[start]=arr[i]
    return arr[:start+1]
arr = [1, 2, 3, 5, 8, 6, 6, 6]
arr.sort()
print(remove_duplicates_sortedarray(arr))
