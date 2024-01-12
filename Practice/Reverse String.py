def reverse_2point(str2):
    str1=list(str2)
    start=0
    end=len(str1)-1
    while start<end:
        str1[start],str1[end]=str1[end],str1[start]
        start+=1
        end-=1
    return ''.join(str1)


print("Reverse of string is",reverse_2point("DSAlgo"))