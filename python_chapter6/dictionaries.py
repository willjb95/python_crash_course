## DICTIONARIES ##
# chapter will be on how to use dictionaries, which allow you to connect pieces of related information
# you can access the information once in a dictionary and how to modify that information. 
# dictionaries can store an alomost limitless amount of information. you can create a dictionary 
# represting a person and then store as much information as you want about them for example
# their name, age, location, profession and any other aspect of a person you can describe.

## A SIMPLE DICTIONARY ##
# consider a game featuring aliens that have different colors and point values. a simple
# dictionary stores information about a particular alien
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# the dictionary alien_0 stores the aliens color and point value
# when we print we specifiy which values to print 

## WORKING WITH DICTIONARIES ##
# a dictionary in python is a collection of key-value pairs. Each key is connected 
# to a value, you can use a key to access the value associated with that key. a keys
# value can be a number, a string, a list, or even another dictionary. in python a 
# dictionary is wrapped in braces {}, with a series of key-value pairs inside the braces
# as shown in an earlier example.

## ACCESSING VALUES IN A DICTIONARY ##
# to gain access to the dictionaries value you give the name and then place the key in square brackets
# like so:
print(alien_0['color'])
# you can have an unlimited number of key-value pairs in a dictionary
new_points = alien_0['points']
print(f"Congratulations, you have just earned {new_points} points!")
# once the dictionary has been defined, the vlaue 'points' in it can be assigned to 
# a variable 'new points'. you can then print statements on how many points they have won.

## ADDING NEW KEY-VALUE PAIRS ##
# dictionarys are dynamic meanin gyou can add key-value pairs at any time.
# to do this you give the name of the dictionary folowed byt the new key in sqaure brackets
# along with a new value, so to expand on our alien_0 dictionary lets add two more key-values
# that show x and y coordinates. coordinates usually start at the upper left of the screen 
# so 0, 25 would set it at the top left 25 pixels down
alien_0['x-position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# this is one method of adding two ney key_value pairs to a dictionary 
# whihc is to add them seperatly 
alien_0 = {'color': 'green', 'points': 5, 
            'x-position': 0, 'y_position': 25}
# this method adds them directly into the dictionary

## STARTING WITH AN EMPTY DICTIONARY ##
# its sometimes convienant or necessary to start with with an empty dictionary and then
# add each item as you go on. to do this define a dictionary with an empty set of brackets
# then add each key_value pair on its own line
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
# you typically use empty dictionaries when storing user-supplied data or when you 
# write code to generate a large number of key-value pairs

## MODIFYING VALUES IN A DICTIONARY ##
# to modify a value in a dictionary, give the name of the dictionary with the key 
# in square brackets and then the new value you want associated with that key
alien_0 = {'color': 'green'}
print(f"This alien is now color {alien_0['color']}") 

alien_0['color'] = 'yellow'
print(f"This alien is now color {alien_0['color']}")
# firstly we have defined a dictionary for alien_0 that contains the color
# we then change the key 'color' to value 'yellow', the output shows this
# has changed to yellow 

# a more interesting example could be tracking the position of an alien that can
# move at different speeds. we will store the value representing the current speed
# and use it to determine how far to the right it should go
alien_0 = {
    'x-position': 0,
    'y-position': 25, 
    'speed': 'medium'
    }
print(f"Original position: {alien_0['x-position']}")

# Move alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == "slow":
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x-position'] = alien_0['x-position'] + x_increment
print(f"New position: {alien_0['x-position']}")

# we define the alien with an initial x position and y position, and speed of medium
# the original x position is printed just to show how far the alien moves
# an if-elif-else chain is used to determine how much it should moved based
# on the current speedusing the variable x_increment which increases each 
# speed, so if the speed of the alien is slow it moves 1 unit to the right.
# once this is calculated the increment is then added onto the original position
# we then print that new position. by changing one value in the aliens dictionary
# you can change the overall behavious which is pretty intereting.

## REMOVING KEY-VALUE PAIRS ## 
# you can use the del statement to completely remove a key-value
# all you need is the dictionary and key you want to del
alien_0['points'] = 100
print(alien_0)
del alien_0['points']
print(alien_0)
# as you can see we added a new key value 'points' to our 
# dictionary and used the del statement followed by dictionary 
# name and key and printed each out 

## A DICTIONARY OF SIMILAR OBJECTS ##
# previous examples have all been different kinds of information
# about one object. you can use them to store info about 
# many objects, say you want to poll people and ask them thier 
# favorutite programming language. a dictionary is useful 
# for storing the results like this 
favorite_language = {
    'sam': 'python',
    'mike': 'c',
    'susan': 'python',
    'lara': 'ruby'
    }
# this dictionary is quite large so we've broken it into 
# several lines. each key is the name of the person asked 
# and the value is which programming lanague they chose 

## USING GET() TO ACCESS VALUE ##
# using keys in square brackets to retrieve a value can 
# cause you to get an error if that value doesnt exist 
# you can use the get() method to set a defualt value
# that is returned if requested key doesnt exist 
point_value = alien_0.get('points', 'No points assigned')
print(point_value)
# if theres a chance that the key you are asking for might 
# not exist then perhaps use the get() method