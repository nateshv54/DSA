def fibonacci(num):
    if num<=1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)
    
if __name__=="__main__":
    n=int(input("Enter a number of terms "))
    if n<=0:
        print("Enter a positive number ")
    else:
        print("Fibonacci sequence: ")
        for i in range(n):
            print(fibonacci(i),end=" ")