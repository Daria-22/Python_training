#My solution

def double_index(my_list,index):
    start = 0
    new_list = []
    for num in my_list:
        if index > len(my_list):
            print ("The index is out of range, the list does not change")
            return my_list
        else:
            if start != index:
                new_list.append(num)
                #print(start,my_list[start])
                start +=1
            else:
                new_list.append(num*2)
                start +=1
    return "This is how the new list looks" + str(new_list)  
#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 1))

#their solution    
'''def double_index(my_list, index):
  # Checks to see if index is too big
  if index >= len(my_list):
    return my_list
  else:
    # Gets the original list up to index
    my_new_list = my_list[0:index]
 # Adds double the value at index to the new list 
  my_new_list.append(my_list[index]*2)
  #  Adds the rest of the original list
  my_new_list = my_new_list + my_list[index+1:]
  return my_new_list'''




    
