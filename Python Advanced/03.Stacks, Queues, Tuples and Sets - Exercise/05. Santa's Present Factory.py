from collections import deque

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
crafted_presents = {}

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

while magic and materials:
    material = materials.pop()
    magic_lvl = magic.popleft()

    result = material * magic_lvl

    if result in presents:
        toy = presents[result]
        if toy in crafted_presents:
            crafted_presents[toy] += 1
        else:
            crafted_presents[toy] = 1
    elif result < 0:
        materials.append(material + magic_lvl)
    elif result > 0:
        materials.append(material + 15)
    else:
        if material == 0 and magic_lvl == 0:
            continue
        if material == 0:
            magic.appendleft(magic_lvl)
        else:
            materials.append(material)

if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or \
        ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")
for key, value in sorted(crafted_presents.items()):
    print(f'{key}: {value}')