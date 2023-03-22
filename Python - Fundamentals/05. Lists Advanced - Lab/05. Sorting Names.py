names = input().split(', ')
sorted_list = sorted(names, key=lambda name: (-len(name), name))
print(sorted_list)
