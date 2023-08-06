#Initial data
#types of haircuts
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

#prices per each haircut
prices = [30, 25, 40, 20, 20, 35, 50, 35]

#number of haircuts last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#resolved tasks for coding
#1. loop for finding average price
total_price = 0
for price in prices:
  total_price += price
number_of_items = len(prices)
print(number_of_items)
print (total_price)
average_price = total_price/number_of_items 
#Output average price
print("Average Haircut Price: "+ str(average_price))

#reducign the price by 5 by "comprehension list"":
reduced_prices= [price -5 for price in prices]
print(prices)
print(reduced_prices)

#finding total revenue for last week and average revenue per day
total_revenue = 0
#loop for prices and number of customers, iterates through both
#gets product of price and purchases and adds to total revenue
for i in range (len(hairstyles)):
  for i in range(len(prices)):
    revenue_for_each = prices[i] * last_week[i]
    #print(prices[i] * last_week[i])
    total_revenue += revenue_for_each
    daily_avrg_revenue = total_revenue/7
print("Total Revenue: " + str(total_revenue))
print("Average Daily Revenue: " + str(daily_avrg_revenue))

#filter out only 30-dollar haircuts by comprehension list
cuts_under_30 = [
  hairstyles[i] for i in range(len(hairstyles)) 
  if reduced_prices[i] < 30]
print (f"Hairstyles which cost under 30{cuts_under_30}") 
#print(reduced_prices)
#print(hairstyles)

