goal = float(input())
balance = float(input())
cons_spendings = 0
days = 0

while balance < goal:
    action = input()
    amount = float(input())
    days += 1
    if action.lower() == "save":
        balance += amount
        cons_spendings = 0
    elif action.lower() == "spend":
        if amount >= balance:
            balance = 0
        else:
            balance -= amount
        cons_spendings += 1
        if cons_spendings == 5:
            break

if balance >= goal:
    print(f"You saved the money for {days} days.")
else:
    print(f"You can't save the money.\n{days}")