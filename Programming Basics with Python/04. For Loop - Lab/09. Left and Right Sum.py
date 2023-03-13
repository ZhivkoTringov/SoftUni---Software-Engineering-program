num = int(input())
left_sum = 0
right_sum = 0
for i in range(2 * num):
    current_num = int(input())
    if i < num:
        left_sum += current_num
    else:
        right_sum += current_num
diff = abs(left_sum - right_sum)
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
elif left_sum != right_sum:
    print(f'No, diff = {diff}')