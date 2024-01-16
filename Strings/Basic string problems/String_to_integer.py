def string_to_integer(s1):
    res = 0
    sign = 1
    i = 0

    if s1[i] == '-':
        sign = -1
        i += 1
    elif s1[i] == '+':
        i += 1
    
    # Convert remaining characters to integer
    while i < len(s1) and s1[i].isdigit():
        res = res * 10 + (ord(s1[i]) - ord('0'))  # Corrected this line
        i += 1
    
    return sign * res

s = '-123'
print(string_to_integer(s))