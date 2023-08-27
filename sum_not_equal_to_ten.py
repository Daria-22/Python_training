def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False

print("The sum of input numbers does not equal to 10:", not_sum_to_ten(9, -1))
# should print True
print("The sum of input numbers does not equal to 10:", not_sum_to_ten(9, 1))
# should print False
print("The sum of input numbers does not equal to 10:", not_sum_to_ten(5,5))
# should print False