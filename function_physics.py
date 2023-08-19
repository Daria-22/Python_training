# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
#convert Fahrenheit to Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp
#test
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

#convert Celsius to Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp
#test
c0_in_fahrenheit = c_to_f(1)
print(c0_in_fahrenheit)
#function to get force mass * acceleration
def get_force(mass, acceleration):
  return mass * acceleration
#testing work of get_force function
train_force = get_force(train_mass, train_acceleration)
#outputting the result of train force calculation
print(f"The GE train supplies {train_force} Newtons of force")
#function to get energy mass * c squared
def get_energy(mass, c= 3*10**8 ):
  return mass * c **2
#testing function get_energy()
bomb_energy = get_energy(bomb_mass)
#outputting the work of bomb
print(f'A 1kg bomb supplies {bomb_energy} Joules.')
#function to calculate work moving transport
def get_work(mass, acceleration, distance):
    work = get_force(mass, acceleration) * distance
    return work
#testing calculation of work of transport
train_work = get_work(train_mass, train_acceleration, train_distance)
#outputting work of train
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")


