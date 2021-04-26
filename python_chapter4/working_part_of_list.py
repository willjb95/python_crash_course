## WORKING WITH PART OF A LIST ##
# chapter 3 was about how to access single elements in a list and in this chapter i have been learning how to work through 
# all the elements in a list. its also possible to work with a specific group of items in lists which python calls "slice"

## SLICING A LIST ##
# to make a slice you specify the index of the fist and last elements you want to work with, as with the range() function
# python stops one item before the second index you specify
coffee = ['kenco', 'azera', 'nescafe', 'costa', 'rave']
print(coffee[0:3])
print(coffee[1:4])
print(coffee[2:8])
print(coffee[:3])
# if you omit the first index python will automatically start your slice at the beginning 
print(coffee[2:])
# if you want all the items from item 3 then you start with index 2 and omit the second index to includes all items after 3
# you can add a third value in the brackets and that will decide how many items to skip between items in the list

## LOOPING THROUGH A SLICE ## 
## you can use a slice in a "for loop" if you want to loop through a subset of the elements. example 
print("These are my 3 favorite coffee's:")
for coffees in coffee[:3]:
    print(coffees.title())
# instead of looping through the entire list it only loops the first 3 values, slices are very useful in a number of situations 
# examples of this are if you wanted to add a players final score to a list everytime they finished playing, you could then get
# the players top three scores by sorting the list in decreasing oder and taking a slice that includes just the first three scores

## COPYING A LIST ##
# common practise is to start with an existing list and make an entirely new list based on the first one. to copy a list
# you can make a slice that includes the entire original list by omitting the first and second index ([:]) this tells python to
# make a list that start at the first item and ends at the last, producing a copy of the list.
fav_shows = ['office', 'queens gambit', 'mandalorian']
friend_shows = fav_shows[:] # without the [:] python would associate these list as one in the same and changing one would change the other
print(f"My favorite shows are:\n {fav_shows}")
print(f"My friends favorite shows are: \n{friend_shows}")
# i have created two lists, one for my fav shows and one for my friends and copied mine using the ([:]). printed a message to show they 
# are the same
fav_shows.append('new girl')
friend_shows.append('hollyoaks')
print(f"My favorite shows are:\n {fav_shows}")
print(f"My friends favorite shows are: \n{friend_shows}")
# now I have appended them to show they are actually different entities. so the lists will now look different 



