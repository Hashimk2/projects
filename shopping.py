# Shopping cart program
#
# Objective: 
#             - User enters foods
#             - User enters price for the food
#             - User can quit
#             - At the end, display all the foods and and total price
#
# Use list to store foods, and prices
# do something UNTIL a condition happens 
#
#
# Get the food from user
# while user did not input q:
#   get the price from user ## Hashim, explain why we get the price 
# over here and not above the while loop?
#   add the food and price to the lists
#   get the food from user ## Hashim, we do we get the food from user here? 
# Also, why do we not get the price from here?
#
# foods are in a list
# prices are in a list
#
# foods = ['Apple', 'Banana', 'Pear']
# Display the foods
#   - Use print
# for food in foods:
#   print(food)
#
# prices = [10.00, 2.00, 3.00]
# total_price = 0
# 
# prices[0] until last_price 
# for price in prices:
#   total_price = price + total_price
#
# print(total_price)

foods = []
prices = []
total = 0

food_input = input('Please enter a food to buy (press q to end): ')
while (food_input != 'q'):
  price_input = float(input('Enter the price of the food: '))

  foods.append(food_input)
  prices.append(price_input)

  food_input = input('Please enter a food to buy (press q to end): ')

for food in foods:
  print(food)

total_price = 0
for price in prices:
  total_price += price

print(total_price)
# foods = []
# prices = []
# total = 0

# food_input = input('Please enter a food to buy (press q to end): ')
# if (food_input != 'q'):
#   print(food_input)
# else:
#   price = float(input('Enter the price of the food: '))