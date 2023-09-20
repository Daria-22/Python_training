#Write your function here
def odd_indices(my_list):
    index = 1
    odd_list = []
    while index < len(my_list):
       odd_list.append(my_list[index]) 
       index +=2
    return odd_list


#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))


'''def odd_indices(my_list):
  new_list = []
  for index in range(1, len(my_list), 2):
    new_list.append(my_list[index])
  return new_list'''
  
