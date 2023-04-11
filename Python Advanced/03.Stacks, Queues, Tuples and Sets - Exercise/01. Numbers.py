first_set = set([int(x) for x in input().split()])
second_set = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0]

    if command == 'Add':
        if line[1] == 'First':
            [first_set.add(int(x)) for x in line[2::]]
        else:
            [second_set.add(int(x)) for x in line[2::]]
    elif command == 'Remove':
        if line[1] == 'First':
            first_set = first_set.difference([(int(x)) for x in line[2::]])
        else:
            second_set = second_set.difference([(int(x)) for x in line[2::]])
    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
