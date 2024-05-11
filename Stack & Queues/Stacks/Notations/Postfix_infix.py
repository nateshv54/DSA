def postfix_to_infix(expression):
    stack = []
    
    for token in expression:
        if token.isalnum():
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append("({}{}{})".format(operand1, token, operand2))
    
    return stack.pop()

# Example usage
postfix_expression = "ab+c*d/"
print("Postfix expression is:", postfix_expression)
print("Infix expression is:", postfix_to_infix(postfix_expression))

'''
Postfix expression is: ab+c*d/
Infix expression is: (((a+b)*c)/d)
'''