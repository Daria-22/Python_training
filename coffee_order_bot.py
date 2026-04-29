def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  res1 = res.lower()
 
  if res1 == 'a' or res1 =='A':
    return 'small'
  elif res1 == 'b' or res1 =='B':
    return 'medium'
  elif res1 == 'c' or res1 =='C':
    return 'large'
  else: 
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response, please.")
    get_size()

def get_drink_type():
  res = input('What type of drink would you like?\n [a] Brewed Coffee\n [b] Mocha\n [c] Latte')
  if res == 'a' or res =='A':
    return 'brewed coffee'
  elif res =='b' or res =='B':
    return 'mocha'
  elif res =='c' or res =='C':
    return  order_latte()
  else:
    print_message() 

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk\n[b] Non-fat milk\n[c] Soy milk")
  if res == 'a' or res == 'A':
    return 'latte'
  elif res == 'b' or res == 'B':
    return 'non-fat latte'
  elif res == 'c' or res =='C':
    return 'soy latte'
  else: 
    print_message()
    order_latte()


def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  #print(drink_type)
  print(f'Allright, that is {size} {drink_type}.')



# Call coffee_bot()!

coffee_bot()
