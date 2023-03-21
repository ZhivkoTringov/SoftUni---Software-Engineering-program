def palindrome_nums(nums):
    res = []
    for polindrome in nums:
        if polindrome == polindrome[::-1]:
            result = 'True'
            res.append(result)
        else:
            result = 'False'
            res.append(result)
    return res


numbs = input().split(', ')
print(' \n'.join(palindrome_nums(numbs)))
