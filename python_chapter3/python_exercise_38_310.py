# Q: thinks of five places in the world you would like to visit 
poi = ['hawaii', 'bali', 'new zealand', 'santorini', 'amalfi']
# so i have stored my five places i would like to visit in a list named poi(places of interest)
print(poi)
# here i am printing my list to make sure it is printing in the order its currently in
print(sorted(poi))
# i want to print the list out in aplhabetical order without affecting the actual list wo i have used the sorted() function
print(poi)
# to show my list is still in its original order i have printed it again 
poi.reverse()
print(poi)
# this will print my list in it's reverse order
poi.reverse()
print(poi)
# and if we reverse it again it will go back to its original order 
poi.sort()
print(poi)
# using the sort() method has changed the order of the list permanently 
poi.sort(reverse=True)
print(poi)
# using sort() with reverse=True changes the list so its in reversed alphabetical order 

# Q: working with the program from exercise 3-4 to 3-7, use the len() to print a message indicationg the number of people i am inviting
guest_list = ['edward', 'john','hannah', 'elaine']
guest_size = (len(guest_list))
print(f"This is how many guests have I invited to my dinner: {guest_size}.")
# I have copied my guest list over and created a variable guest_size to store the lens() of the guest list, then i print a message with said variable in

# Q: Think of something you could store in a list, for example a list of mountains or rivers. write a program that creates a list
# containing these items and then uses each function introduced in this chapter at least once
fav_food = ['pizza', 'pasta', 'steak', 'crisps', 'veg', 'noodles']
print(fav_food[3].upper())
print(fav_food[3].lower())
print(f"My favorite food is: {fav_food[0].title()}")
fav_food[5] = 'sweets'
print(fav_food)
fav_food.append('noodles')
print(fav_food)
fav_food.insert(3,'burgers')
print(fav_food)
del fav_food[7]
print(fav_food)
popped_food = fav_food.pop(1)
print(f"I no longer like {popped_food}, so I have removed it from my list")
print(fav_food)
unhealthy = ('sweets')
fav_food.remove(unhealthy)
print(f"The {unhealthy} were too unhealthy so I removed it from my list")
print(fav_food)
print(sorted(fav_food))
fav_food.reverse
print(fav_food)
food_amount = len(fav_food)
print(f"This is how many items are left in my list: {food_amount}")