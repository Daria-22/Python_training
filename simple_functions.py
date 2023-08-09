# Write your code below: 
def calculate_expenses(plane_ticket_price, car_rental_rate,hotel_rate, trip_time):
  car_rental_total = trip_time * car_rental_rate
  hotel_total = (hotel_rate * trip_time) - 10
  
  print("Total cost of the trip is " + str(hotel_total + car_rental_total + plane_ticket_price)+'$')


calculate_expenses(200,100,100,5)