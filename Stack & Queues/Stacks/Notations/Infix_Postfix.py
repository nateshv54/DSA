def infix_postfix(expression):
    precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
    stack=[]
    postfix=[]
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char==' (':
            stack.append(char)
        elif char==')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence.get(char,0) <= precedence.get(stack[-1],0):
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    return "".join(postfix)


infix_expression="a+b/(c-d)*e^f"
print("Infix expression is : ", infix_expression)
print("Postfix expression is ",infix_postfix(infix_expression))