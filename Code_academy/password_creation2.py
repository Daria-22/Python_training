def password_generator(first_name,last_name):
  part1 = first_name[-3:]
  part2 = last_name[-3:]
  new_account = part1 + part2
  return new_account


temp_password = password_generator ("Reiko", "Matsuki")
print(temp_password)
