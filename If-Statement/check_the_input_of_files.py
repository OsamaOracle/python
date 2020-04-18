#salnum() function in Python programming language checks whether all the characters in a given string is alphanumeric or not.
filename = open("strings.txt", "r")
content = filename.readlines()
filename.close()

for line in content:
    if(line.replace("\n", "").isalnum()):
        print(line, "was ok.")
    else:
        print(line, "was invalid.")
