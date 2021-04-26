## LOOPING THROUGH AN ENTIRE LIST ##
# you often need to run through all entries in a list performing the same task with each item, when you want to do this you can
# use pythons "for loop"
# lets say we have a list of friends names and we want to print out eah of their name in the list. you could retrive each name
# from the list individually but this would be make it repetitive with a long list of names and we would have to change our code
# each time the list lengths changed. a for loop avoids this ny letting python manage these internally
names = ['josh', 'dave', 'sarah', 'jodie']
for name in names:
    print(name)
# what I have done here is defining a list of names in variable "names" , the next line we define a for loop. this line tells python
# to pull a name from the list names and associate it with name. we then tell python to print the name that has just been assigned
# to name. python then repeats this once for each name in the list. it can be viewed as "for every name in the list of names, print the names name"

## A CLOSER LOOK AT LOOPING ##
# the concept of looping is important because it one of the most common ways a computer automates repetitive tasks. for name in names tells 
# python to retrive the first name in the list and reads the next line which is print() so it prints the current value. the first value is josh 
# because he list contains more values python returns to the first line of the loop which is "for name in names" and so on until no values left

## DOING MORE WORK WITHIN A FOR LOOP ##
# you can do just about anything with each item in a "for loop" like building on my first example by printing each name a message
# keep in mind that you need to use the indented line that follows the loop for it to work properly 
for name in names:
    print(f"Hello {name.title()}, I hope you are well?")
    print(f"Good {name}, I am happy you are well.\n")
# because you have indented both calls to print(), each line will be executed once for every name in the list, so the first
# value will get asked both those questions first and then onto the second. the newline is to seperate each persons message. 

## DOING SOMETHING AFTER A LOOP ##
# any lines of code after the for loop that are not indented are executed once without repetition
# whenj you are processing data using a for loop you will find a print() function at the end not indented will be a good way to summerize

## AVOIDING INDENTATION ERRORS ##
# python uses indentation to determine how a line, or group of lines , is related to the rest of the program. in the previous code the lines that printed the
# messages to the individuals were part of the "for loop" because they were indented. pythons use of indentation makes it very easy to read.
# you need to watch out for a few common indentation errors, for example accidently indenting a line of code or forget to.
for name in names:
print(name)
# this will give you an indentation error: expected an indentated block 
for name in names:
    print(name)
print(f"I look for to seeing you later, {name.title()}!")
# this print() is supposed to be indented but because python finds atleast one indented line after the "for" statement, it doesnt report an error
# the second print() is not indented so this acts as if it's not in the "for loop" and just prints the one message to one individual 

## INDENTING UNNECESSARILY ## 
# if you indent a line of code that doesnt need to be indented then python lets you know of the unepected incident 
hello_world = "Hello World!"
    print(hello_world)
# we don't need to indent this because it isnt part of a loop, so only indent when you need to and have a specific reason too

## INDENTING UNNECESSARILY AFTER THE LOOP ##
# if you accidently indent code that should run after the loop has finished, that code will be repeated once for each item in the list
# this sometimes prompts python to report an error like so 
for name in names:
    print(f"I hope you have enjoyed your day, {name.title()}.")
    print(f"That is good, I can't wait to see you again, {name.title()}.\n")

    print("Thank you all for the nice responses")
# this shows it is printed for each person in the list 

## FORGETTING THE COLON ## 
# the colon at the end of the for statement tells python to interpret the next line as the start of the loop
# if you accidentally forget the colon, you will always get a syntax error because python doesnt know what youre trying to do 