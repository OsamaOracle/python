def main():
    while True:
        userinput = input("Write something (quit ends): ")
        if(userinput == "quit"):
            break
        elif "X" in userinput:
            print(userinput)
            print("X Spotted!")
        else:
            tester(userinput)


def tester(givenstring="Too short"):
    if(len(givenstring) <= 10):
        print("Too short")

        return False
    #elif(len(givenstring) > 10) :
    else:

        print(givenstring)
        return False
  # elif "X" in givenstring:
        #for i in givenstring:
          #  if i == "X":
             #   print(givenstring)
              #  print("X Spotted!")
              #  return True


if __name__ == "__main__":
    main()