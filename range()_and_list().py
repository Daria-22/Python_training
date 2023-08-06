# Your code below: 
#create range
number_list = range(9)

#print range (pay attention, output will be 0 and 9)
print(number_list)
#Output range(0, 9)

#for printing all the components in the range, use built-in  list() method
print(list(number_list))
#Output  [0, 1, 2, 3, 4, 5, 6, 7, 8]

##another example:
zero_to_seven = range(8)
print(zero_to_seven)
print(list(zero_to_seven))

#range with defines start (first 2), finish (9) and skip(second 2)
my_range2 = range(2, 9, 2)
print(list(my_range2))

#range starts at 0, finishes before 40, skips in 5
range_diff_five = range(0, 40, 5)
print(range_diff_five)
print(list(range_diff_five))


# Your code below:
single_digits = range(10)
squares  = []
for digit in single_digits:
  print(digit)
  for digit in single_digits:
    squares.append(digit * digit)
print(squares)
    
'''0
1
2
3
4
5
6
7
8
9
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81] '''
  