#If Sum of Factors==Num then Perfect Number

def PerfectNum(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum

n=int(input("Enter a Number: "))
print("Perfect Number") if n==PerfectNum(n) else print( "NOt a Perfect Number")
