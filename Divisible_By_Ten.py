# Write your divisible_by_ten() function here:
def divisible_by_ten(num):
    if num % 10 == 0:
      return True
    else:
      return False

print("Is the input number divisible by 10?:", divisible_by_ten(20))
# should print True
print("Is the input number divisible by 10?:", divisible_by_ten(25))
# should print False