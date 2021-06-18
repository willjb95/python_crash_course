# Q1: Use a dictionary to store information about a person you know
# invclude, first name, last name, age and city they live in.
# and print each piece of information in the dictonary
friend_0 = {
    'first_name': 'Brian',
    'Last_name': 'Song',
    'Age': 27,
    'city': 'Cambridge'
    }

print(friend_0)

# Q2: use a dictionary to store peoples favorite numbers.
# have five names and think of a favorite name for each
# print each name with their favorite number
fav_numbers = {
    'jack': 7,
    'simon': 28,
    'kathy': 68,
    'nigel': 12,
    'keith': 36
}

print(fav_numbers)

# Q3: think of five programming words you have learned 
# about in previous chapters. use them as keys and store
# their meanings as values. print each word and meaning 
# neatly formatted 
glossary = {
    'class': 'Code template for creating objects',
    'variable': 'Reserved memory location to store values',
    'syntax': 'Sets of rules that defines how a python program interpets',
    'tuples': 'Stores mutiple items in a single variable',
    'if statements': 'Examines the current state of a program and respond'
}

print("\nHere is an explanation of five programming words I have learned:\n")
print(f"Class - {glossary['class']}.")
print(f"Variable - {glossary['variable']}.")
print(f"Syntax - {glossary['syntax']}.")
print(f"Tuple - {glossary['tuples']}.")
print(f"If Statement - {glossary['if statements']}.")