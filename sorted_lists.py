#Write your function here
def combine_sort(my_list1,my_list2):
  new_list = sorted(my_list1 + my_list2)
  return new_list

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#Output: [-10, 2, 2, 4, 5, 5, 10, 10]