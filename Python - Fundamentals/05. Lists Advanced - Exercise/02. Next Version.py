version = [int(num) for num in input().split('.')]
version[-1] += 1
for current_ver in range(len(version) - 1, -1, -1):
    if version[current_ver] > 9:
        version[current_ver] = 0
        if current_ver - 1 > 0:
            version[current_ver -1] += 1
print('.'.join(str(num) for num in version))
