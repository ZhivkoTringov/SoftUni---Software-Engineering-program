set_of_nums = input().split(' ')
num_counter = int(input())
new_list = []
final_list = []
for i in set_of_nums:
    new_list.append(int(i))
j = 0
min_num = 0
for j in range(len(new_list)):
    if j >= num_counter:
        break
    if min(new_list):
        min_num = min(new_list)
        new_list.remove(min_num)
print(*new_list, sep=', ')
