num_usernames = int(input())
usernames = set()
for _ in range(num_usernames):
    usernames.add(input())
for i in usernames:
    print(i)