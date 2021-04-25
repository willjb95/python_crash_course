# most lists you create will be dynamic meaning you will build a list and then add and remove elements as your program runs its course
# an example would be if you were to create a game where you shoot down alien ships, you could store the initial set of ships ina  list and then 
# remove one as they get shot down.

## MODIFIYING ELEMENTS IN A LIST ##
# the syntax for modifying an element is similar to the syntax for ccessing an element in a list, to change an element use the name of the list
# followed by the index of the element you want to change then provide the new value you want that item to have 
seasons = ['spring', 'summer', 'fall', 'winter']
seasons[0] = 'winter'
print(seasons)

## ADDING ELEMENTS TO A LIST ##
# you might want to add a new element to a list for many reasons. an example would be making new aliens appear in a game, add new data to a visualization
# or add new registered users to a website you've built
# simplist way to add an item to a list is to append the item to the list, when you do this the new element is added to the end of the list 
seasons.append('spring')
print(seasons)
# the append method makes it easy to build list dynamically, you can start with an empty list then add items using item.append
cars = []
cars.append('peugeot')
cars.append('vauxhall')
cars.append('honda')
cars.append('bmw')
print(cars)
# building a list this way is very common because you often won't know the data your users want to store in a program until after the program
# is running. to put users in control, start by defining an empty list that will hold the users value then append each new value to the list 