key_materials = {'shards': 0, 'fragments': 0, 'motes':0 }
obtained = False
data = input().split(' ')
while True:
    for i in range(0, len(data), 2):
        value = int(data[i])
        key = data[i + 1].lower()
        if key not in key_materials:
            key_materials[key] = 0
        key_materials[key] += value
        if key_materials['shards'] >= 250:
            print('Shadowmourne obtained!')
            key_materials['shards'] -= 250
            obtained =True
        elif key_materials['fragments'] >= 250:
            print('Valanyr obtained!')
            key_materials['fragments'] -= 250
            obtained =True
        elif key_materials['motes'] >= 250:
            print('Dragonwrath obtained!')
            key_materials['motes'] -= 250
            obtained =True
        if obtained:
            break
    if obtained:
        break
    data = input().split(' ')
for key, value in key_materials.items():
    print(f'{key}: {value}')