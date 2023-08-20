# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > num2 * 2:
    return True
  else:
    return False
print(f'The first number is twice as large as the second number ,{twice_as_large(10, 5)}')
# should print False
print(f'The first number is twice as large as the second number ,{twice_as_large(11, 5)}')
# should print True