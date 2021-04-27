## IF STATEMENTS 2 ##
# when you understand conditional tests, you cant start writing if statements, several
# kinds of these exist, and the choice depends on the number of conditions you need to test

## SIMPLE IF STATEMENTS ## 
# the simplist kind of if statement has one test and one action
    # if conditional_test:
    # do something  
# you can put any conditional test in the first line and just about any action in the 
# indented block following it. it python deems it true it then executes the code, and if
# false python doesnt. say we have a variable representing a persons age and we know
# the person is old enough to vote 
age = 19

if age >= 18:
    print("This person is old is old enough to vote")
# python checks to see if the age if greater or equal to 18, if so python executes print()
# indentation plays th same role as for loops, all indented lines will be executed if the
# test passes 
    print("Don't forget to vote")
# the conditional test passes so both print() calls that are indented are executed 

## IF-ELSE STATEMENTS ##
# often you will want to take one action when a conditional test passes and a different
# action in all other cases. pythons if-else syntax makes this possible. 
else:
    print("Sorry, you are not old enough to vote")
# if the test evaualtes to false the else block will execute, so if age in lower than 18
# the else block will print()

## THE IF-ELIF-ELSE CHAIN ##
# often you need to test more than two posibilities. for this we can use the if-elif-else syntax
# python only executes one block in this chain, it runs each test in order until one passes 
# when a test passes the following code is executed, many real world situations involve more
# than two possibilties - 
# admissions for under age 4 is free
# admissions for between ages 4 and 18 is 25
# admissions for age over 18 is 40
age_0 = 12

if age_0 < 4:
    print("Your ticket will be free")
elif age_0 < 18:
    print("Your ticket will be £25, please")
else:
    print("Your ticket will be £40")
# the if tests whether the person is under 4, if it were to pass then that block of code following
# would print. the elif line is just another if test which runs only if the previous test failed
# which it did. that then passes because the age is under 18 so the following block executes
# a more consise way of writing this is to just set the price inside the the if-elif-else chain
# and than have a simple print() call that runs after the chains evaluated

if age_0 <4:
    price = 0
elif age_0 <18:
    price = 25
else:
    price = 40

print(f"Your admission fee is £{price}.") 
# here you can see we set the value of price according to the person's age. we then use a seperate
# print() call to use this value to display the message. this way is easier to modify and easier to
# read. to change the the text output you would only need to change the price value.

## USING MULTIPLE ELIF BLOCKS ##
# you can use as many elif blocks in your code as you need. if the amusement park from the previous
# example were to implement a discount for seniors you could add one more conditional test to 
# determine whether they qualified for senior discount, say 65 or older pays half the price.

if age_0 <4:
    price = 0
elif age_0 <18:
    price = 25
elif age_0 <65:
    price = 40
else:
    price = 20

print(f"Your admission fee is £{price}.")
# most of the code is unchanged. the second elif block now checks to see if the person is under 65
# which they are not so it assigns then the full admission rate of 40. we then change the value of 
# else because the only ages that make it to this block are people 65 or over.

## OMITTING THE ELSE BLOCK ##
# python does not require an else block at the end of an if-elif-else. sometimes it is clearer to
# use an additional elif statement that catches the specific condition of interest.

if age_0 <4:
    price = 0
elif age_0 <18:
    price = 25
elif age_0 <65:
    price = 40
elif age_0 >65:
    price = 20

# the else block matches any condition that wasn't matched by a specific it or elif and that can
# sometimes include invalid or even harmful data. if you have a specific final condition in mind
# consider using the final elif block and omit the else block 
