first_sequence = input().split(', ')
second_sequence = input().split(', ')
new = []
for i in first_sequence:
    for j in second_sequence:
        if i in j and not i in new:
            new.append(i)
print(new)