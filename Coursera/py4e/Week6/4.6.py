# Week 6 assignment 4.6
# Writing a function to compute workers pay

# function definition 
def computepay(hrs, rate):
    overtime = hrs - 40
    overtimeRate = rate * 1.5
    if hrs == -1:
        return -1
    p = ((hrs - overtime)*rate + (overtime * overtimeRate))
    return p

hours = input("please enter the hours: ")
rate = input("please enter the rate: ")

# exception handling
try:
    ihrs = float(hours)
    irate = float(rate)
except:
    ihrs = -1
    irate = -1

# calling the function
pay = computepay(ihrs, irate)
print("Pay", pay)
