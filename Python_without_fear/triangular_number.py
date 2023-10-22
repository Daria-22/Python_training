number  = int(input("Input your number which is > 0"))
if number <=0:
    print("Enter a correct number, please")
else:
    start_number = 0
    triangular_number = 0
    while start_number <= number:
        triangular_number += start_number
        start_number+=1
    print(triangular_number)
        
        