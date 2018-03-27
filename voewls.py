voewls = 0
consonants = 0
ask = input("Please enter your word here?! ").strip()

for letter in ask:
    if letter.lower() in "aeiou":
        voewls = voewls + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1

print ("There are {} vowels".format(voewls))
print ("There are {} consonants".format(consonants))



