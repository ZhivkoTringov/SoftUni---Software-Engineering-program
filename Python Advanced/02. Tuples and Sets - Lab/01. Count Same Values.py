nums = [float(x) for x in input().split()]
seq = {}
for i in nums:
    if i not in seq:
        seq[i] = []
    seq[i].append(1)
for key, value in seq.items():
    print(f'{key} - {len(value)} times')