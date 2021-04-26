# Q: if you could invite anyone to dinner who would you invite and make a list that includes at least three  people, then use 
# that list to print a message to each guest individually 
guest_list = ['edward', 'john','hannah']
guest_invite = "I would like to invite you to dinner,"
print(f"Hi, {guest_invite} {guest_list[0].title()}?")
print(f"Hi, {guest_invite} {guest_list[1].title()}?")
print(f"Hi, {guest_invite} {guest_list[2].title()}?")
# I have created a guest list and created a invite message which will be the same for all three guest. but when i print 
# make make sure to add their names using the index for eah guest

# Q: one of the guest cant make it so you need to send a new set of invitations, add print() call at the end of the program stating the
# name of the guest who cant make it - modify your list, replacing the name of the guest wo cant make it with the name of the new person -
# print a second set of invitations, one for each person still on the list
print(f"Sorry everyone, {guest_list[1].title()} can not make it to dinner!")
del guest_list[1]
guest_list.insert (1,'elaine')
print(f"Hi, {guest_invite} {guest_list[1].title()}?")
# so i send out a message stating john could not make it then i deleted his name from the list and replaced it with my new guest 
# and now i am able to send out a new invite to my new guest 

# Q: you have just found a bigger dinner table, so now more spaces are available, invite three more guests. add a print() call to the end
# informing everyone that you found a bigger dinner table - use insert() to add one new guest to the beginning of your list - use insert() 
# to add one new guest to the middle of you list - use append() to add one new guest to the end of your list - print a new set of invites for
# each person in your list
print(f"Hello, {guest_list}, just to inform you we now have a bigger table. That means three more guests can join!")
guest_list.insert(5,'harry')
guest_list.insert(0,'danny')
guest_list.append('jack')
print(guest_list)
invite_old = "I would like to invite you to dinner? There will now be six of us."
invite_new = "now there is more room at the dinner table I am able to invite you, fancy it"
print(f"Hi, {invite_new} {guest_list[0].title()}?")
print(f"Hi, {invite_old} {guest_list[1].title()}")
print(f"Hi, {invite_new} {guest_list[2].title()}?")
print(f"Hi, {invite_old} {guest_list[3].title()}")
print(f"Hi, {invite_old} {guest_list[4].title()}")
print(f"Hi, {invite_new} {guest_list[5].title()}?")
# started by sending out a message to the three current guests informing them there is a bigger table so three more guest can be invited
# so we add the three new guest to our curretn list, 2 by insert() and 1 by append(). I print to make sure it all looks good, now we create 
# two new variables one to store a message for the original three guests and one to store a message for the new three guests. use the fstring 
# to print two different variables with new and old going to respective guest 

# Q: the dinner table will not arrive in time for the dinner so you can now only have two guests - add a new line that prints a message saying
# you can only invite two guests - use pop() to remove guests from your list one at a time until you onyl have two names remaining, each time
# you pop a name from that list, print a message to that person letting them know you're sorry you cant invite them - print a message to 
# each of the two people left in your list, letting them know they are still invited - use del to remove that last two names from your list 
# so you have an empty lsit, print your list to make sure you have an empty list.
print("Sorry to everyone who was invited to dinner, the table will not arrive in time so I can only have two guests now")
# using the print() to send a message to everyone stating I can only invite 2 guests 
uninvited = "Sorry I can not invite you anymore"
# created a variable to store the uninvited message so i dont have to write it out 4 times
guest_popped0 = guest_list.pop(0)
print(f"{guest_popped0.title()}, {uninvited}.")
guest_popped1 = guest_list.pop(0)
print(f"{guest_popped1.title()}, {uninvited}.")
guest_popped2 = guest_list.pop(2)
print(f"{guest_popped2}, {uninvited}.")
guest_popped3 = guest_list.pop(2)
print(f"{guest_popped3}, {uninvited}.")
# popped the fours guests i had no room for out of the list and stored then in a variable and so i can then send a message to that individual 
print(f"Hello, {guest_list[0].title()} and {guest_list[1].title()}, you are still invited to the dinner party.")
# printing a new meesage to the remaining 2 guests stating they are still able to join by using the index feature to show both names 
del guest_list[0]
print(guest_list)
del guest_list[0]
print(guest_list)
# deleted the remaining two guest, once you pop a value then the following one will take that position hence why there are both index[0]
# i printed the list just to make sure no one is left on it 


