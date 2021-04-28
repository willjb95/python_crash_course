users = ['mike', 'sam', 'baz', 'york', 'ant']
banned_users =['tom', 'lewis', 'harry', 'york']

for banned_user in banned_users:
        if banned_user not in users:
            print(f"Sorry {banned_user.title()}, you are still banned.")
        else:
            print(f"Congratulations {banned_user.title()}, you are now unbanned")

# reverse a list 
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
numbers = numbers[::-1]
print(numbers)

# another example of exercise 5-10
group_0s = ['cathy', 'BETH', 'sam',
             'owen', 'lenny']

group_1s = ['bard', 'beth', 'lenny', 
            'simon', 'kurt', 'SAM']

group_0_lower = [group.lower() for group in group_0s] # "group.lower()" can be any word e.g user, person
                                                      # we have created a new list which will replace group_0s

for group_1 in group_1s: # here we choose group_1 as the list we want to loop 
    if group_1.lower() in group_0_lower: # instead of writing group_0s we now write group_0_lower
        print(f"{group_1.title()} is taken")
    else:
        print(f"{group_1.title()} is not taken")






