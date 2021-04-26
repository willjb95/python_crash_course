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

## INSERTING ELEMENTS INTO A LIST ##
# you can add a new element at any point in your list by using the insert() method, you do this by specifying the index of the new element
cars.insert(4,'audi')
print(cars)
# this inserts the value at the end of the list, the insert() method opens a space at position 4 and store the value 'audi' at that location

## REMOVING ELEMENTS FROM A LIST ##
# often you will want to remove an item or set of items from a list, examples would be if a player shoots down an alien ship from the sky
# you'll most likely want to remove it from the list of active ships or when a user decides t cancel there account on a web application
# you created, you will want to remove the user from a list of active users, there are a few ways to do this 

## REMOVING AN ITEM USING THE DEL STATEMENT ##
# i you know the position of the item you want to remove from the list you can use the del statement 
del cars[4]
print(cars)
# this causes the last car we added to the list to be deleted 

## REMOVING AN ITEM USING THE POP() METHOD ##
# sometimes you will want to use the value of an item you have removed from a list, for example you might want the x, y position of an alien ship
# you have just shot down so you can draw an explosion at the bottom. in a web enviroment you might want to remove the user from active users and
# add them to a list of inactive users. the pop() method removes the last item of the list but it lets you work with that item after you have used it
popped_cars = cars.pop()
print(cars) 
print(popped_cars)
# we started by popping a value from the list and storing it in the variable popped_cars, we then print a list to show the value has been removed and then 
# print the popped value to prove we still have access to the value. this could be useful if the list was in chronological order of when we owened each car
last_owned = cars.pop()
print(f"The last car I owned was a {last_owned.title()}!")

## POPPING ITEMS FROM ANY POSITION IN A LIST ##
# you can use pop() to remove an itwm from any position ina list by including the idex of the item you want to remove
first_owned = cars.pop(0)
print(f"The first car I owned was a {first_owned}!")
# the best way to decide on whether to use a del statement or a pop() statement is as follows, when you want to delete a item from a list and not use it in any way
# use the del statement but if you want to use the value you delete use the pop() function.

## REMOVING AN ITEM BY VALUE ##
# sometimes you wont know the position of the value you want to remove from a list, if you only know the value thenyou will want to use remove()
cars.insert(2,'seat')
print(cars)
cars.remove('seat')
print(cars)
# i added a new value to the list and decided i no longer wanted it so i removed it by using its value instead of position
# you can also use the remove() method to work with a value thats being removed, for example print a reson behind 
cars.insert(2,'lambo')
too_expensive = "lambo"
cars.remove(too_expensive)
print(f"\n The {too_expensive.title()} was too expensive for me to afford!")
# we added a new car to the list and assign that to the variable called too_expensive, we then tell python we want the value in that variable to be removed 
# but still accessible though the variable too_expensive as to allow us to print a statement about why we removed it from our list 