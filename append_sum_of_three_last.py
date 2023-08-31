#Write your function here
'''def append_sum (my_list):
    real_length = len(my_list)
    index_length = real_length - 1
    while index_length >= 2:
        sum = my_list[index_length] + my_list[index_length-1]
        my_list.append(sum)
        index_length = index_length - 1
    return my_list


print(append_sum([1, 1, 2]))'''

'''def append_sum(my_list):
    real_length = len(my_list)
    print("Real initial length of the list", real_length)
    last_index = real_length - 1
    print("The last index is the list", last_index)
    print("Last two items in the list", my_list[last_index],',', my_list[last_index -1])
    while last_index >= 2 and last_index <= 4 :
        new_sum = my_list[last_index] + my_list[last_index - 1]
        print("Sum of the last two items", new_sum)
        my_list.append(new_sum)
        print("My list after appending", my_list)
        last_index = len(my_list) - 1
        print("Now the last index is", last_index)
        print("Now the last item in the list is ", my_list[last_index])
        
    return my_list

x = append_sum([1, 1, 2])
print(x)'''

#other solution without loop

def append_sum(my_list):
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  return my_list
  

print(append_sum([1, 1, 2]))

