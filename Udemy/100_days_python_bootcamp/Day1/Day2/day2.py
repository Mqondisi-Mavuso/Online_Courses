#Day 2 project {100 days python bootcamp} 10 February 2022
# tip calculator
print("Welcome to the tip calculator")

# get input from the user and type cast it to the correct float values we can use for calculations later
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

#calculte the individual bill and round the answer to two decimal places using the round function
individual_bill = round((bill/number_of_people) +(bill/number_of_people)* (tip/100) , 2)

# using f-string and the print function, output the individual bill
print(f"Each person should pay: ${individual_bill}")
