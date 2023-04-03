statement = list(input())
stack = []
for i in range(len(statement)):
    stack.append(statement.pop())
print(''.join(stack))
