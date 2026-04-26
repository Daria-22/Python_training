#  list of names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Using map with a lambda function to get the length of each name
name_lengths = list(map(lambda x: len(x), names))

# Using map with a defined function to capitalize each name
def capitalize_name(name):
    return name.upper()

capitalized_names = list(map(capitalize_name, names))

# Print the results
print("Original names:", names)
print("Name lengths:", name_lengths)
print("Capitalized names:", capitalized_names)

surnames = ['green', 'smith', 'blacksmith', 'reddington', 'paddington']

def capitaliseSurname(surname):
  return surname.upper()

surnamesUpper = map(capitaliseSurname, surnames)

fullName = list(map(lambda x, y: x + " "+ y, names, surnamesUpper))
print(fullName)
