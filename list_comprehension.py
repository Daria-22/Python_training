#list comprehension
#new_list = [<expression> for <element> in <collection>]
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [number + 10 for number in grades]
print (scaled_grades)

superannuation_sums = [5000*0.10, 6000 *0.10, 5500* 0.10]
original_superannuation_sums = [num*10 for num  in superannuation_sums]
new_superannuation =[num*1.105 for num  in original_superannuation_sums]
print(new_superannuation)

#no_if = [element * 2 for element in collection ]
#if_only = [element * 2 for element in collection if element < 0]
#if_else= [element * 2 if element < 0 else element * 3 for element in collection ]

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
'''We have defined a list heights of visitors to a theme park. In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters.Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.'''
can_ride_coaster = [height for height in heights if height >161]
print(can_ride_coaster)
