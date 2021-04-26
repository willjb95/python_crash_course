## TUPLES ##
# lists work well for storing collections of items that can change throughout the life of a program. the aility to 
# modify lists is when working with lists of users, sometimes you create a list of items that cannot change, tuples
# allow you to do that. python refers to values liek that as immutable and an immutable list is called a tuple.

## DEFINING A TUPLE ##
# a tuple looks just like a list except you use parentheses instead of square brackets, once you define a tuple you
# can acess individual elements by using each items index for example if i have a rectangle that needs to stay the same
# size i can ensure that its size doesnt change by putting the dimensions into a tuple
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
# I define the dimensions using the parentheses instead of square brackets. i print each element in the tuple individually
# using the same syntax i've been using to access elements. lets see what happens if i try and change one of the items in 
# the tuple dimensions 
################# dimensions[0] = 250
################# print(dimensions)
# this cases an error in the terminal because we are trying to alter a tuple which cant be done
# tuples are techincally defined by a comma but parentheses make them look neater and easier to read 

## LOOPING THROUGH ALL VALUES IN A TUPLE ##
# i can loop over all the values in a truple using a for loop
for dimension in dimensions:
    print(dimension)
# python returns all the elements in the tuple as it would in a list

## WRITING OVER A TUPLE ## 
# although you cant modify a tuple, you can assign a new value to a variable that represents a tuple
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,200)
print("\nUnmodified dimensions:")
for dimension in dimensions:
    print(dimension)
# I print the inital dimensions using a for loop and then associate a new tuple with the variable "dimensions". I then print
# the new dimensions, no errors because reasigning a variable is valid 
# when compared with lists, tuples are simple data structures. should be used when needing to store a set of values that should not be changed

