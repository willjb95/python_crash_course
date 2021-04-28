## USING IF STATEMENTS WITH LISTS ##
# combining if statements and lists can lead to very interesting things. for example
# manage chaning availability of certain items in a restaurant throughout a shift

## CHECKING FOR SPECIAL ITEMS ##
# previously we handled special value 'bmw' which needed to be printed in a different format
# no we shalll take a closer look at how you can watch for special values now that we have
# a better understanding of conditional tests and if statements. lets use the pizza topping
# example again

toppings = ['mushrooms', 'cheese', 'pepperoni']

###  for topping in toppings:
###    print(f"Adding {topping.title()}!")
# this is a simple for loop. but lets say one of the toppings has run out of a topping.

for topping in toppings:
    if topping == 'mushrooms':
        print("Sorry, we are out of mushrooms.")
    else:
        print(f"Adding {topping.title()}.")
print(f"Your Pizza is complete!")

# this time we checked each requested item before adding it. the else block ensures all other
# toppings are added.

## CHECKING A LIST THAT IS NOT EMPTY ##
# so far we've assumed each list has had at least one item in the list. what if the users provide
# the information thats stored in a list? we won't be able to assume anymore. in this case its helpful 
# to check if the list has any items stored. 

requested_toppings = []

if requested_toppings: 
    for requested_topping in requested_toppings:
        print(f"Adding {requested.topping}.")
    print("\nFinished making your pizza.")
else:
    print("Are you sure you want a plain pizza?")

# thsi time the list is empty and so instead of going straight into a for look we do a quick check.
# if a name of a list is used in an if statement, python returns true if the list contains at least one item. 
# if there is no list it will return false. so therefor the else block gets executed

## USING MULTIPLE LISTS ##
# this time lets have each item in requested_toppins checked against the list of available toppings

available_toppings = ['mushrooms', 'cheese', 'pepperoni',
                       'peppers', 'olives']
requested_toppings = ['mushrooms', 'cheese', 'chicken']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping.title()}.")
    else:
        print(f"Sorry, {requested_topping.title()} is not availiable.")
print("Finished making your Pizza!")

# first we define a listof avaialble toppings, then a list of requested toppings. This could be a tuple 
# if the selection was static. we then loop through the list of requested toppings, this loops checks whether
# the requested toppings are in the avaliable toppings list. if it is the topping is added, if not the else block 
# will execture true and prints the message telling the user which topping is unavailable