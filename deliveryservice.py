weight = 6.1
way_of_delivery = 4

flat_charge_ground = 20.00
flat_charge_ground_premium = 125.00


if way_of_delivery == 1:
  if weight <= 2.0:
    cost_of_delivery = weight * 1.5 + flat_charge_ground
    print('Cost of delivery is', cost_of_delivery) 
  elif weight > 2.00 and weight <=6.0:
    cost_of_delivery =weight * 3.0 + flat_charge_ground
    print('Cost of delivery is', cost_of_delivery) 
  elif weight > 6.0 and weight <= 10.00:
    cost_of_delivery =weight * 4.0 + flat_charge_ground
    print('Cost of delivery is', cost_of_delivery) 
  elif weight > 10.00:
    cost_of_delivery =weight * 4.75 + flat_charge_ground
    print('Cost of delivery is', cost_of_delivery)     

elif way_of_delivery == 2:
  cost_of_delivery = flat_charge_ground_premium 
  print('Cost of delivery is', cost_of_delivery) 

elif way_of_delivery == 3:
  if weight <= 2.0:
      cost_of_delivery = weight * 4.5
      print(cost_of_delivery) 
  elif weight > 2.00 and weight <=6.0:
      cost_of_delivery = weight * 9.0
      print(cost_of_delivery) 
  elif weight > 6.0 and weight <= 10.00:
      cost_of_delivery = weight * 12.0
      print(cost_of_delivery) 
  elif weight  > 10.00:
      cost_of_delivery = weight * 14.5
      print(cost_of_delivery)  

else:
  print('Please read the instruction carefully')
