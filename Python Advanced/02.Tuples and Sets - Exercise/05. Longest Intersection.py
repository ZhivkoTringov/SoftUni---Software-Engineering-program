def gen_seq(range_info):
    star, end = [int(x) for x in range_info.split(',')]
    return set(range(star, end + 1))


n = int(input())

best_intersection = set()

for _ in range(n):
    line = input().split('-')
    left_side = gen_seq(line[0])
    right_side = gen_seq(line[1])
    current_intersection = left_side.intersection(right_side)

    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection

print(f'Longest intersection is [{", ".join(str(x) for x in best_intersection)}] with length {len(best_intersection)}')