readfile = open("file.txt", "r")
content = readfile.readlines()

#print("the following is the file output :  ")

for i in content:
    print(i)

readfile.close()
