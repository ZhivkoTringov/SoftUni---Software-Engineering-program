name = input()
vowels =['a', 'o', 'u', 'e', 'i']
new = [x for x in name if x.lower() not in vowels]
print(''.join(new))
