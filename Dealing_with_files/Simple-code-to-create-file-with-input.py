filename = input("Give a file name :")
fileinput = input("Write something :")

myfile = open(filename,"w")
myfile.write(fileinput)
myfile.close()

print ("Wrote",fileinput, "to the file",filename)
