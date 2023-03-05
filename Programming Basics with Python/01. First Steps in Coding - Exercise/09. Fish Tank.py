length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = length * width * height
liters = volume * 0.001
needed_liters = liters * (1 - percent / 100)
print(needed_liters)