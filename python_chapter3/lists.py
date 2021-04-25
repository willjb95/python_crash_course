## LISTS ##
# lists are a collection of items in a particular order. you can make a list that includes the letters of the alphabet, digits from 0-9, or the names of all the people in your family
# these items dont have to be related in any way because a list usually contains more than one element. in python square brackets [] indicate a list
# the individual elecments in the list are seperated but commas.
months_of_year = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months_of_year)
# if you ask python to print a list, python returns it representation of the list, including the square brackets. this wouldnt be the output you want users to see

## ACCESSING ELEMENTS IN A LIST ##
# lists are ordered collections, so you can access any item in a list by telling python the position or index of the item. you would write the name of the list followed by
# the index of the item enclosed in the brackets e.g
print(months_of_year[0].upper())
print(months_of_year[5].lower())
# Index positions start at 1 NOT 0 because python considers the first item in a list to be position 0, this is to do with how the list operations are implemented at a lower level 
# python has a special syntax for accessing the last element of a list by asking for index -1
print(months_of_year[-1])
# This is quite useful because you might want to access the last item in a list without knowing exactly how long the list is and this extends to finding the second last item by using index -2
print(months_of_year[-2])

## USING INDIVIDUAL VALUES FROM A LIST ##
# you can use individual values from a list as you would 