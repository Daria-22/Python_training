def more_than_n(my_list, item, n):
    number_of_item = my_list.count(item)
    print(number_of_item)
    if number_of_item > n:
        return True
    else:
        return False
    
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))