#week 5 assignment 3.3
#give the grade between 0.0 and 1.0 print out the grade

score = input("Enter Score: ")
#exception handling
try:
    fscore = float(score)
except:
    fscore = -1
if (fscore == -1):
    print("invalid score!")
elif (fscore > 1.0):
    print("out of range")
elif (fscore >= 0.9):
    print("A")
elif (fscore >= 0.8):
    print("B")
elif (fscore >= 0.7):
    print("C")
elif (fscore >= 0.6):
    print("D")
elif (fscore < 0.6):
    print("F")
