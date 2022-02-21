# day 9/100 days python bootcamp with Dr. Angela Yu
# Given the year and the month, this program will print out the number of days in that month
def is_leap(year):
    """ Takes the year and return true if it's a leap year
    , returns False if it's not a leap year  """
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(given_year, given_month):
    """ Takes in year and month and and returns the number of days in that month  """
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  isLeap = is_leap(year)
  number_of_days = 0

  #checking for clean input
  if given_month < 1 or given_month > 12:
      return "Invalid month input"
  elif given_year < 0:
      return "Invalid year input"

  # checking for a leap year number of days in February
  if isLeap and given_month == 2:
    number_of_days = month_days[given_month - 1] + 1
    return number_of_days
  else:
    number_of_days = month_days[given_month - 1]
    return number_of_days

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
