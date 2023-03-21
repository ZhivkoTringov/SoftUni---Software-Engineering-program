def divisor_sum(num):
    sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sum += divisor
    if num == sum:
        return 'We have a perfect number!'
    return "It's not so perfect."


number = int(input())
print(divisor_sum(number))