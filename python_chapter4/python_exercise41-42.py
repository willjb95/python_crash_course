# Q: think of at least three kinds of pizza - store these names in a list and ther use "for loop" to print the name of each pizza -
# modify the "for loop" to print a sentance using the name of the pizza instead of just the name of the pizza, should include one
# simple output for each pizza - add a line at the end outside of the loop that states how much you like pizza, this should consist 
# of three or more lines about the kinds of pizza you like and an additional sentence such as i really love pizza
pizzas = ['margherita', 'pepperoni', 'pineapple']
for pizza in pizzas:
    print(pizza)
# I have created my list of pizza and used the "for loop" to print each pizza name 
for pizza in pizzas:
    print(f"I really like {pizza.title()} pizza!")
print(f"They are all my favorite if I'm honest!")

# Q: think of at least three animals that have a common characteristic, store the names in a list then use "for loop" to print out 
# each name - modify the program to print a statement about each animal, such as a dog would make a great pet - add a line at the end 
# stating what these animals have in common 
animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print(animal.title())
    print(f"{animal.title()}s are very energetic!")
print(f"\nThese animals would all make great pets!")