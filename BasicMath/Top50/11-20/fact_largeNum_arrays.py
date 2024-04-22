def factorial_of_largeNum_using_arrays(n):
    result=[1]
    for i in range(2,n+1):
        carry=0
        for j in range(len(result)):
            product=result[j]*i+carry
            result[j]=product%10
            carry=product//10
        while carry:
            result.append(carry%10)
            carry//=10
    return result

n=int(input("Enter a number : "))
result=factorial_of_largeNum_using_arrays(n)
result.reverse()
print(f"The factorial of {n} is : {''.join(map(str,result))}")
