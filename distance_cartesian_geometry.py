#distance_cartesian_geometry.py

'''x1 = float(input("Enter x1, please"))
x2 = float(input("Enter x2, please"))
y1 = float(input("Enter y1, please"))
y2 = float(input("Enter y2, please"))
leg1 = x1 - x2
print(f"Leg1 is {leg1}")
leg2 = y1 - y2
print(f"Leg2 is {leg2}")
hypotenuse = round(((leg1 ** 2 + leg2 ** 2) ** 0.5),2)
answer = 'Hypotenuse is {}.'
print(answer.format(hypotenuse))'''

#calculates the area of a triangel with a right angle
'''def calculate_triangle_area(width,height):
    area = width * height * 0.5
    string_answer = 'The area of the triangle with such sides is {}.'.format(area)
    print(string_answer)

calculate_triangle_area(50,60)'''

#calculates the area of a cicle
import math
def calculate_the_circle_area(radius):
    radius = float(input("Enter the radius in cm"))
    area = round((math.pi * radius **2),2)
    print("The area of the circle with the given radius is ", area,'.', sep='')
    
calculate_the_circle_area(40)


    