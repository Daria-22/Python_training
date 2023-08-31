# Write your always_false function here:
def always_false(num):
    if num > num:
        return False
    elif(num < num):
        return False
    else:
        return False
    
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
    
    