# Write your dog_years function here:
def dog_years(name, age):
  dogs_age = str(age * 7)
  answer_str = name + ", you are " + dogs_age + " years old in dog years."
  return answer_str
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"