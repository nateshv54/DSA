def even_odd(num):
    if num&1==0:
        return "Even"
    else:
        return "Odd"
    
n=int(input("Enter a number: "))
print("Even Odd",even_odd(n))