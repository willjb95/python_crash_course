## LOOPING THROUGH A DICTIONARY ##
# dictionaries can contain a few or millions of key-value pairs
# because of this python lets you loop through a dictionary 

## LOOPING THROUGH ALL KEY-VALUE PAIRS ##
# lets consider a new dictionary to store information about a user on a website
# this could store username, first and last name 
user_0 = {
    'username': 'pwned',
    'first': 'Nigel',
    'last': 'Frost'
}
# you can access any info about user_0 based on what we've learned.
# but to see everythign stored in this user_0's dictionary you could
# use a for loop 
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
# to write a loop for a dictionary you can create names for the two
# variables that hold key and value, can choose any names for these
# abbreviations would also work. then the name of the dictionary 
# followed by the method items() which returns a list of key-value
# pairs. the for loop assigns each of these pairs to the two variables
# the \n ensure a new line is printed before each key-value pair

# this for loop would be sueful for a previous example, the favorite 
# languages dictionary 
favorite_language = {
    'sam': 'python',
    'mike': 'c',
    'susan': 'python',
    'lara': 'ruby'
    }

for name, language in favorite_language.items():
    print(f"\n{name.title()}'s favorite programming language is {language.title()}")
# the descriptive names make it much easier to see what the print() call
# is doing. 

## LOOPING THROUGH ALL THE KEYS IN A DICTIONARY ##
