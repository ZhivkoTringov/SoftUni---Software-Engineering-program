from collections import deque
num_pumps = int(input())
pumps = deque()
for _ in range(num_pumps):
    pump_data = [int(x) for x in input().split()]
    pumps.append(pump_data)
for att in range(num_pumps):
    tank = 0
    failed = False
    for fuel, km in pumps:
        tank +=fuel
        if km > tank:
            failed = True
            break
        tank -= km
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(att)
        break