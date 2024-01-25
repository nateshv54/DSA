from sys import maxsize
#maxsize is used to return -infinite when stack is empty
def createStack():
    stack=[]
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print(item,"pushed to stack")
def pop(stack):
    if isEmpty(stack):
        return str(-maxsize -1)
    return stack.pop()

#function to return top element
def peek(stack):
    if isEmpty(stack):
        return str(-maxsize -1)
    return stack[len(stack)-1]

s=createStack()
print(isEmpty(s))
push(s,3)
push(s,2)
push(s,4)
print(s.pop())
print(peek(s))
print(s)