f_sum = int(input())
s_sum = 0
while True:
    c_num = int(input())
    s_sum += c_num
    if s_sum >= f_sum:
        print(s_sum)
        break