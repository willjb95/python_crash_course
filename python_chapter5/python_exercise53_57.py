# Q5-3 imagine an alien shot down in a game. create a variable called alien_color
# and assign it a value of a green, yellow or red - write an if statement to test
# whether the aliens colour is green, if so print message - write one test that passes
# and one that fails (failed version has no output)

alien_color = 'green'

if 'green' in alien_color:
    print("My alien colour is Green.")
if 'red' in alien_color:
    print("My alien colour is Red.")

# Q5-4: choose a color for an alien again and write an if- else chain -if aliens colour
# is green print statement that player just earned 5 points for shooting the alien - 
# if colour isnt green print statement player earned 10 points - write one version 
# that runs the if block and another than runs the else block

alien_color_0 = 'red'

if 'green' in alien_color_0:
    print("Congratulations, you have earned 5 points!")
else:
    print("Congratulations, you have earned 10 points!")

# Q5-5: turn the if-else chain into a if-elif-else chain - if green print 5 points - 
# if yellow print 20 points - if red print 15 points 

if 'green' in alien_color_0:
    print("Congratulations, you have earned 5 points!")
elif 'yellow' in alien_color_0:
    print("Congratulations, you have earned 10 points!")
else:
    print("Congratulations, you have earned 15 points!")

# Q5-6: write an if-elif-else chain that deterines a person's stage of life. set a 
# variable for the age - if person is less than 2 print baby - if 2 but less than 4
# print toddler - if 4 but less than 13 print kid - if 13 but less than 20 print 
# teenager - if 20 but less than 65 print adult - if 65 or older print elder

age = 40

if age < 2:
    print("Baby")
elif age < 4:
    print("toddler")
elif age < 13:
    print("kid")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Elder")

# Q5-7: make a list of your favorite fruits and then write a series of independent if 
# statements that check for certain fruits in the list - make a list called fav_fruits -
# write five if statements. each should check whether a certain kind is in the list. 

fav_fruits = ['bananas', 'apples', 'oranges']

if 'bananas' in fav_fruits:
    print("Bananas are your favorite.")
if 'grapes' in fav_fruits:
    print("Grapes are your favorite.")
if 'apples' in fav_fruits:
    print("Apples are your favorites.")
if 'peaches' in fav_fruits:
    print("Peaches are your favorite")
if 'oranges' in fav_fruits:
    print("Oranges are your favorite")