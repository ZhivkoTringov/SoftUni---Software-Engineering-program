numbers_of_strings = input().split(', ')
count_of_beggars = int(input())
list_of_integers = []
final_list = []
counter_index = 0
for element in numbers_of_strings:
    list_of_integers.append(int(element))
while counter_index < count_of_beggars:
    sum_of_current_beggar = 0
    for index in range(counter_index, len(list_of_integers), count_of_beggars):
        sum_of_current_beggar += list_of_integers[index]
    counter_index += 1
    final_list.append(sum_of_current_beggar)
print(final_list)