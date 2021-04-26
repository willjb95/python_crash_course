# Q: a buffet-style restaurant offered only five basic food. think of five simple foods and store them in a tuple -
# use a for loop to print each food the resturant offers - try modify one of the items, and make sure that python
# rejects the change - they change the menu, replace two of the items with different food. add a line that rewrites
# the tuple, and then use a for loop to print each of the items on the revised menu 

basic_food = ('pasta', 'bread', 'chicken', 'cake', 'mushroom')
for basic_foods in basic_food:
        print(basic_foods)

## basic_food.append('beef')
## for basic_foods in basic_food:
##      print(basic_foods)
# if i wanted to add another value to the list i would get an error: tuple object has no attribute to append

print("This are what our menu has to offer:")
basic_food = ('pasta', 'bread', 'chicken', 'cake', 'mushroom')
for food in basic_food:
    print(food)

print("\nThis is what our new manu has to offer:")
basic_food = ('pasta', 'garlic', 'pizza', 'cake', 'mushroom')
for food in basic_food:
    print(food)