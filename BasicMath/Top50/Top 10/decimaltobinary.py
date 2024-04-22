def decimal_to_binary(num):
    bin_num=""
    while num>0:
        r=num%2
        bin_num=str(r)+bin_num
        num//=2
    return bin_num if bin_num else "0"

num=15
print(f"The binary form of {num} is {decimal_to_binary(num)}")
