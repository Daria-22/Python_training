#string_letter_check.py

def letter_check(word, letter):
    #start counter of letters
    count = 0
    #iterate through the letters in the word
    for letter_in_word in word:
      #set the condition of search
          if letter_in_word == letter:
            # add to the counter if the letter is found
               count+=1
    #analyse the count, if 0 - then false, if not- then true
    if count > 0:
        return(True)
    else:
        return(False)
#test the function
print(letter_check("strawberry", "a"))
print(letter_check("strawberry", "b"))
print(letter_check("strawberry", "x"))

#My mistake was to ask the function to print(False) instead of explicitly ask it to return the result