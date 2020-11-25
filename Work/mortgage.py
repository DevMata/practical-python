# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
factor = (1 + rate / 12)
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    if payment > principal * factor:
        total_paid = total_paid + principal * factor
        principal = 0
    else:
        principal = principal * factor - payment
        total_paid = total_paid + payment

    months = months + 1

    if extra_payment_start_month <= months <= extra_payment_end_month:
        if extra_payment > principal:
            total_paid = total_paid + principal
            principal = 0
        else:
            principal = principal - extra_payment
            total_paid = total_paid + extra_payment

    print(months, round(total_paid, 2), round(principal, 2))

print()
print('Total paid', round(total_paid, 2))
print('Months', months)
