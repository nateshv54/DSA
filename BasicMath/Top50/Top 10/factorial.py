def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)

if __name__=="__main__":
    n=int(input("Enter a number: "))
    print("Factorial of number: ",factorial(n))