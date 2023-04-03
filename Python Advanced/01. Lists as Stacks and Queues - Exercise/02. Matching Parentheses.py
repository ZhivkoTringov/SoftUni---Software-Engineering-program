expression = input()
stack = []
for i in range(0, len(expression)):
    if expression[i] == '(':
        stack.append(i)
    elif expression[i] == ')':
        start = stack.pop()
        print(expression[start: i+1])