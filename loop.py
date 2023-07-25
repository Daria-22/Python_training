'''for i in range(1,3):
  for j in range(2):
    print("I have " + str(j) + " egg(s)!")
  print("She has " + str(i) + " egg(s)!")'''
  
  
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"
for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed )
  if dog_breed == dog_breed_I_want:
    print ("They have the dog I want!")
    break

