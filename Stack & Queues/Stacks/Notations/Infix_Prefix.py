def infix_to_prefix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    prefix = []
    
    # Reverse the infix expression
    expression = expression[::-1]
    
    for char in expression:
        if char.isalnum():
            prefix.append(char)
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix.append(stack.pop())
            stack.pop()  # Discard the ')'
        else:
            while stack and precedence.get(char, 0) < precedence.get(stack[-1], 0):
                prefix.append(stack.pop())
            stack.append(char)
    
    while stack:
        prefix.append(stack.pop())
    
    # Reverse the prefix expression to get the final result
    return "".join(prefix[::-1])

# Example usage
infix_expression = "(A-B/C) * (A/K-L)"
print("Infix expression is:", infix_expression)
print("Prefix expression is:", infix_to_prefix(infix_expression))

'''
Infix expression is: (A-B/C) * (A/K-L)
Prefix expression is:   -A/BC*-/AKL
'''