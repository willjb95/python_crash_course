## NUMBERS ## 
# numbers are used quite often in programming to keep score in games, represent data in visualizations, store information in web applications 
# and so on, python treats them in different ways depending on how they are being used 

## INTEGERS ##
# you can add (+), subtract(-), multiply(*) and divide(/) integers in python e.g
# the spacing in these has no effect on how python evaluates the expressions, it just helps when reading through the code
a = 5 + 4
b = 500 - 45
c = 8 * 36
d = 356 / 23
print(a,b,c,d)
# python supports the order of operations so you can use multiple operations in one expression, you can also use 
# parentheses to modify the order of operations so python can evaluate them to your specifi requests 
e = 5 + 20 * 4
f = (5 + 20) * 4
print(e,f)

## FLOATS ##
# python calls any number with a decimal point a "float", this is a very common term and refers to the fact that a decimal point
# can appear at any position in a number. for the most part you can use decimals without worrying about how they behave 
g = 0.1 + 0.5
print(g)
# be aware you can get an arbitrary number of decimal spaces, this happens in all languages and is of little concern, we can just ignore them for now
h = 0.2 + 0.1
print(h)

## INTEGERS AND FLOATS ##
# when you divide any two number even if integers you will always get a float 
# and if you mix an integer and a float in anyt other operation you will also get a float, python defualts to a float in any operation that uses a float even the output os a whole number 
i = 2 * 3.0
print(i)

## UNDERSCORES IN NUMBERS ## 
# when writing long numbers you can group digits up using underscores to make large numbers more readable 
# when you print a number that was defined using underscores, python only prints the digits. to python 1_000 is the same as 1000 and works with integers and floats 
universe_age = 14_000_000_000
print(universe_age)

## MULTIPLE ASSIGNMENT ## 
# you can assign values to more than one variale using a single line. this helps shorten programs and makes it easier to read 
# you need to seperate variable names and values with commas and python will assign each value to its respectively posisitioned variable 
j, k, l = 4, 6.7, 133_00_0
print(j, k, l)

## CONSTANTS ## 
# a constant is like a variable whoel value stays the same throughout the life of a program, python doesnt have a built in constant typer but you can 
# use all capital letters to indicate a variable should be treated as a constant and not be changed 
MAX_CONNECTIONS = 4000
print(MAX_CONNECTIONS)