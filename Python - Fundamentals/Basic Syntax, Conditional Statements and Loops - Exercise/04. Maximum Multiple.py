num1 = int(input())
num2 = int(input())
for i in range(num2, num1, -1):
    if i % num1 ==0:
        break
print(i)