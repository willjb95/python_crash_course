# Q: write a series of conditional tests. print a statement describing each test
# and your prediction for each test.

# a bunch of conditional tests with predictions for each
car = 'corsa'
print("Is car == 'corsa'? I predict True")
print(car == 'corsa')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

drink = 'pepsi'
print("\nIs drink == 'pepsi'? I predict True")
print(drink == 'pepsi')

print("Is car == 'coke'? I predict False")
print(drink == 'coke')

pizza = 'pepperoni'
print("\nIs pizza == 'pepperoni'? I predict True")
print(pizza == 'pepperoni')

print("Is pizza == 'pineapple'? I predict False ")
print(pizza == 'pineapple')

football_team = 'chelsea'
print("\nIs football team == 'chelsea'? I predict True")
print(football_team == 'chelsea')

print("Is football team == 'liverpool'? I predict False")
print(football_team == 'liverpool')

sudoku = 'fun'
print("\nIs sudoku == 'fun'? I predict True")
print(sudoku == 'fun')

print("Is sudoku == 'not fun'? I predict False")
print(sudoku == 'not fun')

condiment = 'mustard'
print("\nIs condiments == 'mustard'? I predict True")
print(condiment == 'mustard')

print("Is condiment == 'ketchup'? I predict False")
print(condiment == 'ketchup')

# Q: have one true and false for the following - test for equality and inequality -
# test using the lower() method - numerical test involving equality and inequality
# greater than and less than, greater than or equal to, and less than or equal to -
# test using the "and" keyword and the "or" keyword - test whether an item in a list -
# test whether an iten is not in a list

name_1 = 'will'
name_2 = 'willy'
name_3 = 'william'

# equality of strings 
if (name_1 == name_1):
    print("equal")
else:
    print("unequal")

# inequality of strings 
if (name_2 != name_2):
    print("The names are equal")
else:
    print("The names are unequal")

# test using the lower() method
names = ['will', 'willy', 'william']
for name in names:
    if name == 'will':
        print(name.upper())
    else:
        print(name.lower())

# numerical tests
age_1 = 20
age_2 = 25

# equality of numbers
if age_1 == 25:
    print("equal")

# inequality of numbers
if age_2 != 35:
    print("These numbers are unequal")

# greater than
if (age_2 >= 21): 
    print("They can legally drink")

# less than 
if age_1 <= 21:
    print("They cannot legally drink")

# greater than or equal to 
if (age_1 >= 21) or (age_2 == 40):
    print("Ages 2 is greater than 25 or ages 3 is equal to 40")
else:
    print("Ages 2 is not greater than 25 and ages 3 is not equal to 40")

# less than or equal to
if (age_1 <= 21) and (age_2 == 25):
    print("Person 1 can't legally drink but person 2 can")
else:
    print("Either Person 1 can legally drink or person 2 can't")

# test whether an item is in a list
drinks = ['coke', 'pepsi', 'sprite']

if 'coke' in drinks:
    print("coke is in my drinks list")

# test whether item is not in a list 
if 'monster' not in drinks:
    print("Monster is not in my drinks list")
