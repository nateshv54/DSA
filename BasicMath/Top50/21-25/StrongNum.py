#Factorial of digits Sum==Num then Strong Number
def Digit_Fact_Sum(num):
    sum=0
    while num>0:
        r=num%10
        num//=10
        sum+=factorial(r)
    return sum


def factorial(r):
    if r==0 or r==1:
        return 1
    return r*factorial(r-1)

n=int(input("Enter a Number: "))
print("Strong Number" if n==Digit_Fact_Sum(n) else "Not a Strong Number")

#ex:- 145