import re

txt = input()
searched_word = input()
pattern = fr'\b{searched_word}\b'
matches = re.findall(pattern, txt, flags=re.I)
print(len(matches))