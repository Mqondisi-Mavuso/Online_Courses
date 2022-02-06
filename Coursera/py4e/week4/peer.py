hrs = input("Enter Hours:")
h = float(hrs)
rat = input("Please enter the rate: ")
rate = float(rat)
overtime = h - 40
if h > 40:
    overtimeRate = rate * 1.5
    pay = ((h - overtime) * rate) + (overtime * overtimeRate)
else:
    pay = h * rate
print(pay)
