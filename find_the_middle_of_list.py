#Write your function here
def middle_element(my_list):
    oddOrEven = len(my_list)%2
    if oddOrEven == 0:
        print('This list is even, printing average of two middle elements')
        index1 = int(len(my_list)/2-1)
        #print(index1)
        x1 = my_list[index1]
        #print(x1) 
        index2 = int(len(my_list)/2)
        x2 = my_list[index2] 
        average_number_x1_x2 = (x1 + x2)* 0.5
        #print(average_number_x1_x2)
        return(average_number_x1_x2)
    else:
        print('This list is odd, printing the number in the middle of the list')
        index3=int(len(my_list)/2-0.5)
        #print(index3)
        x3 = my_list[index3]
        return x3
    
    
#Uncomment the line below when your function is done
print(middle_element([5, 2, -4, 4, 5]))