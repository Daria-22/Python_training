def trip_planner(first_destination, second_destination, final_destination ="Codecademy HQ"):
  print('Here is what your trip will look like!')
  print(f'First, we will stop in {first_destination}, then {second_destination}, and lastly {final_destination}')
#positional
trip_planner("France", "Germany", "Denmark")
#positional
trip_planner("Denmark", "France", "Germany")
#keyword aguments
trip_planner(first_destination = "Iceland", second_destination = "India", final_destination = "Germany" )
#2 positional and 1 default (Codeacademy HQ)
trip_planner("Brooklyn", "Queens")