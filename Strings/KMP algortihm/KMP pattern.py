def patternserach(pat,txt):
    m=len(pat)
    n=len(txt)
    i=0
    j=0 
    #initialize lps array of size m with zeroes
    lps=[0]*m
    lpsarray(pat,lps,m)
    while ((n-i)>=(m-j)):
        if pat[j]==txt[i]:
            j+=1
            i+=1
        if j==m:
            print("Pattern found at {}th index".format(i-j))
            
            #set j pointer to position where last character was successfully matched
            j=lps[j-1]

        elif i<n and pat[j]!=txt[i]:
            if j!=0:

                #set j pointer to position where last character was successfully matched
                j=lps[j-1]

            else: # j=0

                #Increment i pointer to move forward in txt
                i+=1



def lpsarray(pat, lps, m):
    l = 0
    # 0th index is always zero, because there is no going back from the beginning of the string
    lps[0] = 0
    j = 1
    while j < m:
        if pat[j] == pat[l]:
            # Matching characters, increment both length of common prefix/suffix and pattern index
            l += 1
            lps[j] = l
            j += 1
        else:
            if l != 0:
                # Mismatch, update l to the length of the longest proper prefix that is also a suffix
                l = lps[l - 1]
                # No increment of j here; effectively "jumping back" in the pattern
            else:  # l == 0
                # Mismatch and no previously found common prefix/suffix, move on to the next character
                j += 1

                

if __name__=='__main__':
    txt = "ABABCDABACDABABCABABC"
    pat = "ABC"
    patternserach(pat,txt)

#Note: LPS- Longest Proper Prefix which also suffix