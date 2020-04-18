##The idea is to create a program which asks for a user name and password.
username = input("Give name: ")
#password = input("Give password: ")

if (username == "John"):
	username = input("Give Password ? ")
	if (username == "ABC123"):
		print ("Both inputs are correct!")
	else:
		print ("The password is incorrect.")
else:
	    print("The given name is wrong.")
