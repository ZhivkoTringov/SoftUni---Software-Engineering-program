num = int(input())
shells = []
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
while True:
    for i in n:
        shell = 2 * (i ** 2)
        if num >= shell:
            shells.append(shell)
            num -= shell
        if 0 < num < shell:
            shells.append(num)
            break
    break
print(shells)
