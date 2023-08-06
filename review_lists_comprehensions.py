# Your code below:
single_digits = range(10) #10 not included!
print(single_digits) #output 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
squares  = []

for digit in single_digits:
  print(digit)
for digit in single_digits:
    squares.append(digit **2)
print(squares)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]]
cubes = [digit **3 for digit in single_digits]    
print(cubes)
#[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
