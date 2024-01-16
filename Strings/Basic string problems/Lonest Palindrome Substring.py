def longestpalindromeSubstring(s1):
    max_str=''
    for i in range(0,len(s1)):
        cur_str=''
        for j in range(i,len(s1)):
            cur_str+=s1[j]
            if palindrome(cur_str) and len(cur_str) >len(max_str):
                max_str=cur_str
        
    return max_str 

def palindrome(s1):
    return s1==s1[::-1]

s1='Raavan'
print(longestpalindromeSubstring(s1))