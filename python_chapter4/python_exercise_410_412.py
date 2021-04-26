# Q: using one of the programs you wrote before, add several lines to the end that do the following - print the
# message "the first three items in the list are" then use a slice to print the first three items - print the 
# message "three items from the middle of the list are" use a slice to print 3 items from the middle of that list
# - print the message "the last three items in the list are" use a slice to print the last three items 
coffee = ['kenco', 'azera', 'nescafe', 'costa', 'rave']
cof_first = coffee[0:3]
cof_mid = coffee[1:4]
cof_last = coffee[2:5]
print(f"The first three items in the list are: {cof_first}") 
print(f"The middle three items in the list are: {cof_mid}")
print(f"The last three items in the list are: {cof_last}")

# Q: start with program from exercise 4-1. make a copy of the list of pizza and call its friends_pizza - add new pizza
# to original list - add different pizza to list of friends - prove that you have two seperate lists. print the message
# "my friends favorite pizzas are:" and then use a for loop to print the second list
pizzas = ['margherita', 'pepperoni', 'pineapple']
friends_pizza = pizzas[:]
friends_pizza.append('vegetarian')
print("My friends faovrite pizzas are:")
for friends_pizzas in friends_pizza:
    print(friends_pizzas)
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

# Q: all versions of food.py have had no for loops to save space. choose a version and write two for loops to print each 
# list of food 
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]
print("\nMy faovrite food:")
for my_food in my_foods:
    print(my_food)
print("\nMy friends favorite food:")
for friends_foods in friends_food:
    print(friends_foods)