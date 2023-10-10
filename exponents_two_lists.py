#simple method to solve:
'''list1 = [6,4,3]
list2 = [6,7,8]
for number in list1:
    print (number, "this is number 1")
    for number2 in list2:
        print(number,"this is number 2")
        number3 = number ** number2
        print(number3, "this is number 3")'''
    
#method to solve with function:
def exponents(bases,powers):
    answers = []
    for number1 in bases:
        print(number1)
        for number2 in powers:
            print(number2)
            number3= number1 ** number2
            answers.append(number3)
    return answers

print(exponents([2, 3, 4], [1, 2, 3]))


'''their solution def exponents(bases, powers):
  new_list = []
  for base in bases:
    for power in powers:
      new_list.append(base ** power)
  return new_list'''