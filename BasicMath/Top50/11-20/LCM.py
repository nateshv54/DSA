def LCM(num1,num2):
    if num1==0 or num2==0:
        return 0
    else:
        gcd=1
        for i in range(1,min(num1,num2)+1):
            if num1%i==0 and num2%i==0:
                gcd=i
        lcm=(num1*num2)//gcd
        return lcm
    
#Recursive appraoch

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)

num1=12
num2=15
print(f"Lcm of {num1} and {num2} is {LCM(num1,num2)}")
print(f"Lcm of {num1} and {num2} is {lcm(num1,num2)}")