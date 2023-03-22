nums_as_strings = input().split(', ')
nums = [int(num) for num in nums_as_strings]
print(f"Positive: {', '.join(str(num) for num in nums if num >=0)}")
print(f"Negative: {', '.join(str(num) for num in nums if num < 0)}")
print(f"Even: {', '.join(str(num) for num in nums if num % 2 ==0)}")
print(f"Odd: {', '.join(str(num) for num in nums if num % 2 !=0)}")
