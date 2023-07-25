#nested loops, this simple thing couldn't be explained to me by my upskilled teacher!!! OMG!
#the list contatins other three lists, they are sales of each location
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
#first loop allows to reach inside the first list and iterate the components
for location in sales_data:
  print("Printing amount of scoops solf for each location in the list")
  print(location)
  for scoop_sold in location:
      scoops_sold += scoop_sold

print(f'Printing total amout of scoops sold in all locations: {scoops_sold}')


