import re
pattern = r'\b_([A-Z-a-z-0-9]+)\b'
txt = input()
matches = re.findall(pattern, txt)
print(','.join(matches))