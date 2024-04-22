def power(num,pow):
    if pow==0:
        return 1
    return num*power(num,pow-1)

n=4
print("Power of number is ",power(n,3))
