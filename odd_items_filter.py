#Write your function here
def odd_indices(my_list):
    index = 1
    odd_list = []
    length = len(my_list)
    while index < (len(my_list)):
       odd_item = my_list[index]
       odd_list.append(odd_item) 
       index +=2
    return odd_list


#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))