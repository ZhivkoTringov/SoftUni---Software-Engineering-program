deposite_sum = float(input())
months = int(input())
annual_rate = float(input())
acc_rate = deposite_sum * (annual_rate / 100)
rate_per_month = acc_rate / 12
total_sum =  deposite_sum + months * rate_per_month
print(total_sum)