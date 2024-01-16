def palindrome(s1):
    return s1.lower()==s1[::-1].lower()

#Two pointer technique
def palindrome2(s1):
    s1=s1.lower()
    start,end=0,len(s1)-1
    while start<end:
        if s1[start]==s1[end]:
            start+=1
            end-=1
        else:
            return False
    return True

s1='Malayalam'
print(palindrome2(s1))