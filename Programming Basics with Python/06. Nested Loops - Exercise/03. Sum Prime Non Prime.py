condition = False
prime_sum = 0
non_prime_sum = 0
while True:
    num = input()
    if num == 'stop':
        break
    num = int(num)
    if num < 0:
        print('Number is negative.')
    else:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    condition = True
                    break
            if condition:
                non_prime_sum += num
                condition =False
            else:
                prime_sum += num
print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')