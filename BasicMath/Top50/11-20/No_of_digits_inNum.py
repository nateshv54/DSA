def NumberOfDigits(num):
    count=0
    while num>0:
        r=num%10
        if r:
            count+=1
        num//=10
    return  count

n=int(input("Enter a number: "))
print(f"No.of digits in {n} are {NumberOfDigits(n)}")