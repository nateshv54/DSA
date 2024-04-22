def sumofdigits(num):
    sum=0
    while num>0:
        r=num%10
        sum+=r
        num//=10
    return sum

n=int(input("Enter a number : "))
print(sumofdigits(n))
