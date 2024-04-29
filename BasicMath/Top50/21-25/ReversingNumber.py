def reverserNum(num):
    rev_num=0
    while num>0:
        r=num%10
        rev_num=rev_num*10+r
        num//=10
    return rev_num

n=654
print("Reverse of number is : ",reverserNum(n))