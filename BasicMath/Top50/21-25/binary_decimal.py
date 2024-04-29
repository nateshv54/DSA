def binary_to_decimal(binum):
    decimal=0
    for i in range(len(binum)):
        decimal+=int(binum[len(binum)-1-i])*(2**i)
    return decimal

n=input("Enter Binary number :")
print(f"Decimal equivalent of {n} is {binary_to_decimal(n)}")
