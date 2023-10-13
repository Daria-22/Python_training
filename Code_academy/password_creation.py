def account_generator(first_name, last_name):
    part1 = first_name[0:3]
    part2 = last_name[0:3]
    newaccount = part1 + part2
    return newaccount

new_account = account_generator("Julie","Blevins")
print(new_account)