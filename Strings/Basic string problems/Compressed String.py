def charcompressed(s, t):
    n = 0
    flag = 1  # Fix: Correct the assignment operator
    j = 0
    for i in range(0, len(t)):  # Fix: Loop over the shorter string 't'
        if t[i] >= '0' and t[i] <= '9':
            n *= 10
            if n > 100000:
                return 0
            n += int(t[i]) - int('0')  # Fix: Convert characters to integers
            j -= 1
        else:
            j += n
            if j >= len(s) or t[i] != s[j]:
                flag = 0
                break
            n = 0

        j += 1
    j += n
    if j != len(s):
        flag = 0
    if flag:
        return 1
    else:
        return 0

#another approach
    
def charcompressed2(s,t):
    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if t[j].isdigit():
            count = 0
            while j < len(t) and t[j].isdigit():
                count = count * 10 + int(t[j])
                j += 1
            i += count
        elif t[j] == s[i]:
            i += 1
            j += 1
        else:
            return 0

    return i == len(s) and j == len(t)
if __name__ == '__main__':
    S = "GEEKSFORGEEKS"
    T = "G7G3S"
    print(charcompressed2(S, T))
