# def odd_digits(number: int):
#     pass
#
#
# def even_digits(number: int):
#     pass


num = (input())
new = []
even = []
odd = []
x = 0
l = 0
for i in num:
    if i.isdigit():
        new.append(i)
for j in new:
    if int(j) % 2 == 0:
        even.append(j)
    else:
        odd.append(j)
for k in even:
    x += int(k)
for y in odd:
    l += int(y)
print(f'Odd sum = {l}, Even sum = {x}')


