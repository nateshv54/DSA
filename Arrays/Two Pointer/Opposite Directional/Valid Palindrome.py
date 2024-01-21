def valid_palindrome(str):
    start=0
    end=len(str)-1
    while start<end:
        if str[start]!=str[end]:
            return False
        start+=1
        end-=1
    return True


print(valid_palindrome(5,"ACACA"))