def firstUniqueCharacter(str):
    no_of_chars=256
    count=[0]*no_of_chars
    #count the frequenct of each character
    for i in range(len(str)):
        if (str[i]!=" "):
            count[ord(str[i])]+=1
    ans=""
    #printing the first non_repeating character in string
    for j in range(len(str)):
        if(count[ord(str[j])]==1):
            ans+=str[j]
            break
    if ans=="":
        return "#"
    return ans

n=int(input("Enter no.of testcases: "))
l=[]
for i in range(n):
      l.append(input())

for i in l:
    print(firstUniqueCharacter(i))