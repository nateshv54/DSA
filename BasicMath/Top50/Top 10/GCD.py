def GCD(n1,n2):
    if n2==0:
        return n1
    return GCD(n2,n1%n2)

def GCD_iterative(n1,n2):
    while n2!=0:
        n1,n2=n2,n1%n2
    return n1

print(GCD_iterative(120,300)) #60
print(GCD(48,18))  #6
