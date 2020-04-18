# Get sentence from user
original = input("What is your sentence ?!").strip().lower()
# Split sentence into words
words= original.split()
print(original)

# loop through words and convert to pig latin

new_word = []
#vowels start with "YAY"

for word in words:
    if word[0] in "aeiou":
      new_add = word + "yay"
      new_word.append(new_add)
    else:
      vowel_pos = 0
      for letter in word:
          if letter not in "aeiou":
             vowel_pos = vowel_pos + 1
          else:
              break

      cons = word [:vowel_pos]
      the_rest = word [vowel_pos:]
      new_add = the_rest + cons +"ay"
      new_word.append(new_add)



#print (new_word)

#merge the words together
output = " ".join(new_word)
print (output)
