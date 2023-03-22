new = input().split(' ')
palindrome_list = []
counter = 0
palindrome_word = input()
for palindrome in new:
    if palindrome == palindrome[::-1]:
        palindrome_list.append(palindrome)
for word in palindrome_list:
    if word == palindrome_word:
        counter += 1
print(palindrome_list)
print(f'Found palindrome {counter} times')