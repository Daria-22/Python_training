#you can get a count of character in a string by:

#def get_length(string):
#  return len(string)

#or

def get_length2(string):
  count = 0
  for letter in string:
    count +=1
  return count

print(get_length2("Daria"))
