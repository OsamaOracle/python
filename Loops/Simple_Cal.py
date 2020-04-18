print ("Calculator")

n1 = int(input("Give the first number:"))
n2 = int(input("Give the second  number:"))

while True:

    print ("(1) +\n(2) -\n(3) *\n(4) /\n(5) Change numbers\n(6) Quit\nCurrent numbers: ", n1,n2)
    choice = int (input("Please select something(1 - 6):"))

    if (choice == 1 ):
        result = n1 + n2
        print ("The result is:", result)
    elif (choice == 2):
        result = n1 - n2
        print("The result is:", result)
    elif (choice == 3):
        result = n1 * n2
        print("The result is:", result)
    elif (choice == 4):
        result = n1 / n2
        print("The result is:", result)
    elif(choice == 5):
        n1 = int(input("Give the first number:"))
        n2 = int(input("Give the second  number:"))
    elif (choice == 6):
        print("Thank you")
        break
    else:
        print ("Selection was not correct.")

