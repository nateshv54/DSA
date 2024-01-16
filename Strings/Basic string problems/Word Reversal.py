def wordreversal(s1):
    s2=[]
    s2=[w[::-1] for w in s1.split()]

    return ' '.join(s2)

s2="Heloo Nice MIc"
print(wordreversal(s2))