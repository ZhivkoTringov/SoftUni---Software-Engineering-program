string1 = input()
string2 = input()
last_str = string1
for i in range(len(string2)):
    left_side = string2[:i+1]
    right_side = string1[i+1:]
    current_str = left_side + right_side
    if last_str == current_str:
        continue
    print(current_str)
    last_str = current_str