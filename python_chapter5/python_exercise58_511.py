# Q5-8: make a list of five or more usernames, including the name admin. print a 
# greeting to each user after they log in to a website. loop through the list
# and print a greeting to each user - if the username is admin print a special
# greeting - otherwise print a generic greeting

usernames = ['admin', 'mike95', 'willjb', 'user1234', 'robbie12']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username.title()}, would you like a progress report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again!")

# Q5-9: add an if test to the users to make sure the list is not empty - if the list is 
# empty print the message we need to find some users - remover usernames to make sure
# it works correctly

usernames = []

if usernames: # this is our if statement to test whether anyone is in the list
    for username in usernames: # this runs a loop through all names in usernames variable and 
                               # will execute the following block if it shows at least one name in the list
        print(f"Thanks {username.title()}, for joining")
    print("That is all the users")
else: # else this block will execute if no names show up because python will deem that as false
    print("We need some more users!")

# Q5-10: Do the following to create a program that simulates how websites ensure everyone has
# a unique username - make a list of five usernames - make another list called new_users,
# make sure two of the usernames are also in users - loop through new_users to see if 
# each user name has been used, if it has print message that person needs new username. if
# username has not been used print message saying user name available - make sure comparison 
# is case insensitive. if john has been use, JOHN should not be accepted

current_users = ['Will', 'Jon', 'Sue',
         'Nigel', 'Sommer']

new_users = ['Ray', 'Sam', 'Will',
             'NIGEL', 'Kit']

current_user_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_user_lower:
        print(f"Sorry {new_user.title()}, that username is already in use. Try another")
    else:
        print(f"Thank you for registering, {new_user.title()} is available.")

# Q5-11: ordinal numbers indicate their position in a list, such as 1st or 2nd. most end in th except 1,2,3
# store numbers 1-9 in a list - loop through the list - use an if-elif-else chain to print the proper 
# ordinal ending for each number.

ordinal_numbers = list(range(1, 10))
print(ordinal_numbers)

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f"{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}th")

