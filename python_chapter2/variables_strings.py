print("Hello world!")
# "Print" and "Hello World" are different colours because the interpreter views them as different functions
# this is called sysntax highlighting.

## VARIABLES ##
# variables can be describes as labels that you can assign a to values #
message = "Hello Python World"
print(message)
# we created a variable called "message" with the value displayed after so we can list that variable to print the value
# here are some rules we have to abid by when it comes to variables:
#    only contain letters, numbers and underscores and can only start with a letter or underscore
#    spaces can not be used but can be seperated by underscores
#    names should be short but descriptive """

## STRINGS ##
# a string is a series of characters, anything inside quotes is considered a string #
name = "william bebbington"
print(name.title())
# title() is a method, these are actions that python can perform on a piece of data. Every method is followed by parentheses
# another is lower(), this is partically useful because you'll want to convert strings to lower case before stroing them

## USING VARAIBLES IN STRINGS ##
first_name = "william"
last_name = "bebbington"
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello, {first_name} {last_name}!"
print(message.title())
# to insert variables into strings,place the letter f immediately before the quotes and put braces around the name 
# of any variable you want to use inside it. These are called f-strings short for format 

## ADDING WHITESPACE TO STRINGS WITH TABS OR NEWLINES ##
# whitspace refers to any nonprinting character such as spaces, tabs, end of lie symbols, whitespace can organise your output so its easier to read
print("python")
print("\tpython")
# to add a tab to the text we would use the charcter comnination "\t"
print("Languages:\nPython\nC\nJavaScript")
# to add a newline in a string you would use the character combination "\n"
# we can combine them together to start a newline and add a tab 
print("Languages:\n\tPython\n\tC\n\tJavaScript\n\t")

## STRIPPING WHITESPACE ##
# extra whitespace can be confusing in our programs, 'python' and 'python ' look the same but to a program these are two different  
# strings. python detects extra speace in 'python ' and considers it significant 
# python can look for extra whitespae on the right or left hand sides of a string, to ensure this use "rstrip()"
favorite_language ="python "
print(favorite_language.rstrip())
# strip() is used to delete all the leading and trailing characters mentioned in its argument
# lstrip() is used to delete all the leading characters mentioned in its argument
# rstrip() is used to delete all the trailing characters mentioned in its argument

## AVOIDING SYNTAX ERRORS WITH STRINGS ##
# a syntax error occures when pythn doesnt recognise a section of your program as valid python code 
# an example would be if you used an apostrophe within single quotes, you will get an error e.g 
# message = 'One of Python's strengths is its diverse community' this should be 
message ="One of Python's strengths is its diverse community"
print(message)
