def palindrome(word, idx):
    if idx == len(word):
        return f'{word} is a palindrome'

    first, last = word[idx], word[-1 - idx]
    if first != last:
        return f'{word} is not a palindrome'

    return palindrome(word, idx + 1)