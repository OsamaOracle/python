
filename = "notebook.txt"
while True:

    print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit\n")
    choice = int(input("Please select one: "))

    if (choice == 1):
        readfile = open(filename, "r")
        content = readfile.read()
        print(content)
    elif (choice == 2):
        readfile = open(filename, "a")
        newtext = input("Write a new note: ")
        readfile.write(newtext + "\n")
        readfile.close
    elif (choice == 3):
        readfile = open(filename, "w")
        readfile.close()
        print("Notes deleted.")
    elif (choice == 4):
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection")
