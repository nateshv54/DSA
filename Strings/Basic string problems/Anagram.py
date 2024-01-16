def anagramcheck(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        char1=[0]*128
        char2=[0]*128
        for i in s1:
            char1[ord(i)]+=1
        for i in s2:
            char2[ord(i)]+=1
        if char2==char1:
            return True
    
    return False

def anagramcheck1(s1,s2):
    return sorted(s1)==sorted(s2)
    
s1='abcd'
s2='dcbe'
print(anagramcheck(s1,s2))
        