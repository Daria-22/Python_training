#list comprehension
#new_list = [<expression> for <element> in <collection>]
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [number + 10 for number in grades]
print (scaled_grades)

superannuation_sums = [5000*0.10, 6000 *0.10, 5500* 0.10]
original_superannuation_sums = [num*10 for num  in superannuation_sums]
new_superannuation =[num*1.105 for num  in original_superannuation_sums]
print(new_superannuation)

