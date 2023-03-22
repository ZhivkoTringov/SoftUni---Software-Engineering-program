my_list = []
while True:
    to_do = input().split('-')
    if to_do[0] == 'End':
        break
    priority = int(to_do[0])
    task = to_do[1]
    my_list.append((priority, task))
sorted_list = [tasks[1] for tasks in sorted(my_list)]
print(sorted_list)