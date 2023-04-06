txt = input()
opening = []
balanced = True
for ch in txt:
    if ch in '([{':
        opening.append(ch)
    elif not opening:
        balanced = False
        break
    else:
        last_opening = opening.pop()
        if f'{last_opening}{ch}' not in '()[]{}':
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")