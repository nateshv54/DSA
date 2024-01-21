def maxAreaContainer(arr):
    start,end=0,len(arr)-1
    area=0
    while(start<end):
        #Calculating max area
        area=max(area,min(arr[start],arr[end])*(end-1))
        if arr[start]<arr[end]:
            start+=1
        else:
            end-=1
    return area


a = [1, 5, 4, 3]
b = [3, 1, 2, 4, 5]
 
print(maxAreaContainer(a))
print(maxAreaContainer(b))

https://www.codingninjas.com/studio/problems/container-with-most-water_873860?leftPanelTabValue=PROBLEM&count=25&page=1&search=container%20with&sort_entity=order&sort_order=ASC&customSource=studio_nav
