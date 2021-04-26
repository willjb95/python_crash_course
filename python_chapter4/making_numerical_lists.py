## MAKING NUMERICAL LISTS ##
# there are many reasons why one would want to store numbers. an example is keeping track of a players high score, in data 
# visualizations, you'll almost always work with sets of numbers, such as temperatures or distances. lists are ideal for storing
# sets of numbers and python provides a veriety of tools to help you work efficiently 

## USING THE RANGE() FUNCTION ##
# pythons range function makes it easy to generate a series of numbers. for example you can use range() function to print a 
# series of numbers 
for value in range(1, 5):
    print(value)
# although this looks like it should print the number 5 it doesnt. it only prints the number 1-4 because of the off-by-one behaviour 
# this function causes python to start counting at the first value you give it, and it stops when it reaches the second value you provide
# because its stops there, the output never contains the end value
for value in range(1, 6):
    print(value)
# as you can see this now print the numer 5 because it is no longer the number we asked python to stop at 

## USING RANGE() TO MAKE A LIST OF NUMBER ##
# if you want to make a list of numbers you can convert the results of range() directly into a list using the list() function. when you
# wrap list() around a call to the range() the output will be a list of numbers 
numbers = list(range(1,7))
print(numbers)
# we can also use range() to tell python to ekip numbers in a given range. if you pass a third argument to range(), python used that value
# as a step size when generating numbers, example
even_numbers = list(range(2,13,2))
print(even_numbers)
# the range value starts a 2, and then adds 2 to that value. it adds 2 repeatedly until it reaches or passes the end avlue
# you can almost create any set of numbers you want to using range() function. 
# if we wanted to make a list of the first 10 square numbers in python, two asterisks (**) represent exponents. an example
squares =[]
for value in range(1,11): # 1, 11 is how many squared numbers we want to show, so the first 10 sqaure numbers would print
    square = value ** 2 # this raises the value to the second power
    squares.append(square) # you could get rid of the line of code above and change this line to "squares.append(value**2)"
print(squares)
# we start with an empty list called squares. we then tell python to loop through each value from 1 to 11 using the range() function
# inside the loop the second power is raised to the second power and assigned to the variable square. each new value is appended to 
# the list squares, finally when the loop has finished the list of squares is printed.

## SIMPLE STATISTICS WITH A LIST OF NUMBERS ##
# a few python functions are helpful when working with lists of numbers for example finding the min, max and sum of some digits 
digits = [1,2,3,4,5,6,7,8]
print(min(digits),max(digits),sum(digits))

## LIST COMPREHENSIONS ##
# the approach earlier which invloved generating the list squares consisted of three or four lines of code. a list comprehension
# allows you to generate this same list in just one line. it combines the "for loop" and the creation of new elements into one line,
# and automatically appends each new element. following our previous program
squares = [value**2 for value in range(1,11)]
print(squares)
# you want to start by using a descriptive name for the list. then open a set od square brackets and define the expression for the values
# you want to store in the new list. the expression here is value**2 which raises the value to the second power. then generate a for
# loop to generate the numbers you want to feed into the expression, this is for value in range(1,11) which feeds the values 1 through 10 
# no colon is used at the end of this expression 