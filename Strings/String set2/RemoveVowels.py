def removeVowels(inputstring):
    v="aeiouAEIOU"
    s=''
    for i in inputstring:
        if i not in v:
            s+=i
    return s

if(__name__=="__main__"):
    n=int(input("Enter no.of Test cases: "))
    l=[]
    for i in range(n):
        i=input("Enter the String: ")
        l.append(i)
    print("After removing vowels from string ")
    for j in l:
        print(removeVowels(j))
        