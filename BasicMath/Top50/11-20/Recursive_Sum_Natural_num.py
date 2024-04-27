def SumOfNaturalNumbers(n):
    if n>0:
        return n+SumOfNaturalNumbers(n-1)
    else:
        return 0
n=int(input("Enter Natural Numbers range: "))
print(SumOfNaturalNumbers(n))
