num_guests = int(input())
reservation_codes = set()
for _ in range(num_guests):
    codes = input()
    reservation_codes.add(codes)
command = input()
while command != 'END':
    if command in reservation_codes:
        reservation_codes.remove(command)
    command = input()
print(len(reservation_codes))
for i in sorted(reservation_codes):
    print(i)