import math
def isprime(num):
    if num<=1:
        return False
    else:
        for i in range(2,math.ceil(math.sqrt(num))+1):
            if num%i==0:
                return False
    return True

if __name__=="__main__":
    n=int(input("Enter a number: "))
    print(print(n,"Is a Prime number") if isprime(n) else n,"is not a prime number")
