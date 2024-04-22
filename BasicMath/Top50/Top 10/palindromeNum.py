def reverse(num):
    rnum=0
    while num>0:
        r=num%10
        rnum=rnum*10+r
        num//=10
    return rnum

n=int(input("Enter a number: "))
print("Reverse of number: ",reverse(n))
        