## IF STATEMENTS ## 
# pythons if statements allow you to examine the currrent state of a program
# and respond approprietely to that state
# this chapter will teach me to write conditional tests, which allow you to 
# check any condition of interest. write simple if statements and how to create
# more complex ones. then apply all this to lists as to write a loop that handles
# items in that list

## A SIMPLE EXAMPLE ## 
# Lets create a simple list with car names in it 
cars = ['honda', 'bmw', 'peugeot', 'vauxhall']
# so the list is created. now say we want to print these and as they are car names 
# we want them printed as a title. except bmw, we want that printed all uppercase
# so we create a "for loop" to loop through a list of cars and then create an if statement
# to look for the value bmw, and print it as uppercase else print the other cars as a title
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

## CONDITION TESTS ##
 # at the very core of an if statement is an expressions that can be evaluated as true or false
 # and is called a conditional test. python uses value true and false to decide whether the 
 # code in a if statement should be executed. if true python runs the code and if false it doesnt 

## CHECKING FOR EQUALITY ##
# conditional tests compare the current value of a variable to a specific value of interest 
# the simpliest conditional test checks whether the value of a variable is eual to the value 
car = 'bmw'
car == 'bmw'
            # True
car = 'audi'
car == 'bmw'
            # false 
# we set the value of car to bmw by using the equal sign and then using the double equal sign 
# the quality operator returns the value true if they match and fase if they do not

## IGNORING CASE WHEN CHECKING FOR EQUALITY ##
# two values with different capitalisation are not considered equal. 
# websites enforce certain rules for data that users enter in a manner for example a site might
# use a conditionl test like this to ensure that very user has a truly unique username, a username
# # such a JOHN will be rejected if any variation of john is already in use 

## CHECKING FOR INEQUALITY ## 
# if you want to determine whether two values are not equal you can combine an exclamation point and equal
# sign (!=). the ! represents not. 
requested_drink = 'coke'

if requested_drink !='pepsi': # if this value is set as 'coke' it will return as false and not run
    print("Hold the pepsi!")
# The second line compares the value of requested drink to the value pepsi. if these values don't match
# python returns true and exacutes the code following the if statement. if the two values match then 
# python returns false and does not ring the code following the if statement.

## NUMERICAL COMPARISONS ##
# testing numerical values is not very difficult 
age = 18
age == 18
# this checks whether the person is 18 years old
# you can also check to see if two numbers are not equal
answer = 23

if answer !=35:
    print("That is not the correct answer, please try again")
# this test passes because the value of answer 23 is not equal to 35 so because it passes the indented 
# code block is executed

## CHECKING MULTIPLE CONDISTION ##
# you may want to check mutiple conditions at the same time. for example sometimes you might need to
# take two conditions to be true to take an action 
# to check whether two conditions are both true simultaneously, use the keyword and to combin the 
# two conditional tests
age_0 = 18
age_1 = 25
age_0 >= 21 and age_1 >= 21
# this example shows how you would check if two people are over 21. which would be false because age_0
# doesnt meet this rrequirement and age_1 does so the overall conditional expression evaluates to false
# to improve readabilty, you can use parentheses around the test but is not requaired 
(age_0 >= 21) and (age_1 >=21)

## USING OR TO CHECK MULTIPLE CONDITIONS ##
# the keyword or allows you to check multiple condistions as well but it passes when either or both of
# the individual pass. it only fails when both tests fail 
age_0 = 21
age_1 = 25
(age_0 >= 24) and (age_1 >= 24)
# this would equal true because at least one of them is correct 

## CHECKING WHETHER A VALUE IS IN A LIST ##
# its important to check whether a list contains a certain value before taking action for ecample you 
# might want to check if a new username already exists in a list of current usernames before completing
requested_drinks = ['coke', 'pepsi', 'sprite']
if 'pepsi' in requested_drinks:
    print("true")
# This would print true because the value pepsi is in the list 

## CHECKING WHETHER A VALUE IS NOT IN A LIST ##
# it can be important to check whether a value is not in a list, in this situation you would use the
# keyword "not". this can be helpful if users are banned from commenting. you can check 
# whether the use has been banned before allowing that person to submit a comment 
banned_users = ['mike', 'andy', 'sam']
user = 'david'

if user not in banned_users:
    print(f"{user.title()}, you can post a comment if you would like.")
# this reads quite clearly. if david is not in the list then print message which means hes not banned

## BOOLEAN EXPRESSION ##
# a boolean experession is just another name for a conditional test. a boolean value is either true or false
# just like a value from a conditional test. this an be used to keep track of a game running
game_active = True
# booloeans provide a efficient way to track the state of a program



