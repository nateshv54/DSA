def longestcommonprefix(arr):
    r=arr[0]
    l=len(r)
    for i in range(1,len(arr)):
        while arr[i].find(r)!=0:
            r=r[:l-1]
            l-=1

            if not r:
                return "-1"
    return r

if __name__ == "__main__":
    input_list = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print("The longest Common Prefix is:", longestcommonprefix(input_list))
    