# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months=0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
while principal > 0:
    months+=1
    new_payment=payment
    if months <= extra_payment_end_month and months >= extra_payment_start_month:
        new_payment=payment+extra_payment
    if principal * (1+(rate/12)) < new_payment:
        new_payment=principal*(1+(rate/12))
        principal=0
        total_paid=total_paid+new_payment
    else:
        principal = principal * (1+(rate/12))-new_payment
        total_paid=total_paid+new_payment
    print(f"{months} {total_paid:,.2f} {principal:,.2f}")
print(f"total paid:{total_paid:,.2f}")
print(f"months:{months}")
# Exercise 1.7
