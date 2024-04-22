def Sum_cube_digits(num):
    sum=0
    while num>0:
        r=num%10
        sum+=r**3
        num//=10
    return sum

n=153
print(n,"is Armstrong" if Sum_cube_digits(n)==n else "Not a Armstrong")
