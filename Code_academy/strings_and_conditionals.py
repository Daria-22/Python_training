def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
        #I did not get the check if the letter was in the list of common!
        #should be more attenticve next time
      common.append(letter)
  return common

print(common_letters("Daria","super-tester"))