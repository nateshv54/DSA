def prefix_to_infix(expression):
    stack = []
    
    for token in expression[::-1]:
        if token.isalnum():
            stack.append(token)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append("({}{}{})".format(operand1, token, operand2))
    
    return stack.pop()

# Example usage
prefix_expression = "+-+AB*CD/EF"
print("Prefix expression is:", prefix_expression)
print("Infix expression is:", prefix_to_infix(prefix_expression))

'''
Prefix expression is: +-+AB*CD/EF
Infix expression is: (((A+B)-(C*D))+(E/F))
'''