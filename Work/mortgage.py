# mortgage.py
#
# Exercise 1.7
mortgage = 500000
rate = .05
payment = 2684.11
total_paid = 0
month = 1
extra_payment_start_month = 12*5 + month
extra_payment_end_month = 12*9
extra_payment = 1000

while mortgage > 0:
    mortgage = mortgage * (1 + rate/12) - payment
    total_paid += payment

    if (month >= extra_payment_start_month and 
        month <= extra_payment_end_month):
        mortgage -= extra_payment
        total_paid += extra_payment

    if mortgage < 0:
       total_paid += mortgage
       mortgage = 0

    print(month, total_paid, mortgage)

    month += 1

print(mortgage, round(total_paid, 2))
print("Months:", month - 1)
