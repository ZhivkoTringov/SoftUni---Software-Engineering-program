num_of_char = int(input())
total = 0
for i in range(num_of_char):
    current_char = input()
    total += ord(current_char)
print(f'The sum equals: {total}')