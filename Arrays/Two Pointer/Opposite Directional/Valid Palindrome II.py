'''
Check if given string is palindrome by deleting one character
'''
def validPalindrome(n: int, s: str) -> bool:
    flag = 0
    start = 0
    end = n - 1

    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        elif s[start] == s[end - 1]:
            flag += 1
            end -= 1
        elif s[start + 1] == s[end]:
            flag += 1
            start += 1
        else:
            return False

    if flag > 1:
        return False
    else:
        return True


print(validPalindrome(6,'ABCBDA'))