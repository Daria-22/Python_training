first_name = "Bob"
last_name = "Daily"

'''first_name[0] = "R"'''
'''this won't work as strings are immutable'''

fixed_first_name = "R" + first_name[-2:]

print(fixed_first_name)