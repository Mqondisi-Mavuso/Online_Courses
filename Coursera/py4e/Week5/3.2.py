# This programme will claculate the pay of employees depending the hours worked & overtimeRate
hrs = input("Enter Hours:")
h = float(hrs)
rat = input("Please enter the rate: ")
rate = float(rat)

overtime = h - 40

#calculate overtime pay for workers who worked more that 40 hours
if h > 40:
    overtimeRate = rate * 1.5
    pay = ((h - overtime) * rate) + (overtime * overtimeRate)
# calculate the normal pay
else:
    pay = h * rate
print(pay)
