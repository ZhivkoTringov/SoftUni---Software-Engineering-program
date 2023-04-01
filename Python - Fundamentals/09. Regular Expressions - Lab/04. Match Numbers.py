import re

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
txt = input()
matches = re.finditer(pattern, txt)
for match in matches:
    print(match.group(), end=' ')