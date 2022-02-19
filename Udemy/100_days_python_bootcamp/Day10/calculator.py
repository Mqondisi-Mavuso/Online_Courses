# day 10/100 of python bootcamp with Angela Yu
# calculator project
# I can still improve it by catching bugs from the user input
from art import logo

#add function
def add(num1, num2):
  return num1 + num2

#substraction function
def subtract(num1, num2):
  return num1 - num2

#division function
def divide(num1, num2):
  if num2 == 0:
    return print(f"Cannot divide by {num2}")
  return num1/num2

#multiplication function
def multiply(num1, num2):
  return num1*num2

#this dictionary will store the functions
# using the key, we can return the stored function in another funtion so that we can pass the parameters for the calculations
operations = {}
operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide

def calculator():
  print(logo)
  num1 = float(input("What's the first number? "))

  should_continue = True
  while should_continue:
    for key in operations:    #prints out all the operations in dict
      print(key)
    symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number? "))
    #use the "symbol" to access the function in the dictiopnary
    # the dictionary will return the correct function depending on the
    #input from the user
    try:
        calculation_function = operations[symbol]
        #store the function output to the variable called answer
        answer = calculation_function(num1, num2)
    except:
        print("Invalid operator")

    print(f" {num1} {symbol} {num2} = {answer} \n")
    if input(f"Type 'yes' if you want to continue with {answer} and 'no' if you want to start a new calculation: ") == 'yes':
      num1 = answer
    else:
      should_continue = False

  calculator()

calculator()
