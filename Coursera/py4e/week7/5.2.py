# Week 7 assignment 5.2
# prompt the user for indefinite numbers and print the largest and smallest

smallest = None
largest = None

while True:
    num = input("Please enter number: ")
    if num == 'done':
        break

    #exceptin handling
    try:
        inum = int(num)
    except:
        print("Invalid input")
        continue
    # for finding the Smallest
    if (smallest is None):
        smallest = inum
    elif smallest > inum:
        smallest = inum

    # for findng the largest
    if (largest is None):
        largest = inum
    elif largest < inum:
        largest = inum
print("Maximum is", largest)
print("Minimum is", smallest)
