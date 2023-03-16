first_num = int(input())
second_num = int(input())
for n in range(first_num, second_num +1):
    odd_sum = 0
    even_sum = 0
    for current_num in range(len(str(n))):
        if current_num % 2 == 0:
            even_sum += int(str(n)[current_num])
        else:
            odd_sum += int(str(n)[current_num])
    if even_sum == odd_sum:
        print(n, end=' ')