#Newton's method for square root approximation
def sqrt(num):
    if num<0:
        raise ValueError("Negative number is sqrt is undefined")
    if num==0:
        return 0
    x=num
    y=(x+num/x)/2
    while y<x:
        x=y
        y=(x+num/x)/2
    return x

num=2
print(f"Square root of {num} is {sqrt(num)}")