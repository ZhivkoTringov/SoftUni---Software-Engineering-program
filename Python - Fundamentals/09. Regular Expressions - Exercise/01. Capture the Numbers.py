import re

pattern = '\d+'
line = input()
while True:
    if line:
        matches = re.findall(pattern, line)
        if matches:
            print(' '.join(matches), end=' ')
        line = input()
    else:
        break