from math import floor

world_record = float(input())
distance_m = float(input())
time_for_one_meter = float(input())
time_for_swim = distance_m * time_for_one_meter
resistance_time = (floor(distance_m / 15)) * 12.5
total_time = time_for_swim + resistance_time
diff = abs(world_record - total_time)
if world_record > total_time:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')