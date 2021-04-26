## LOOPING THROUGH AN ENTIRE LIST ##
# you often need to run through all entries in a list performing the same task with each item, when you want to do this you can
# use pythons "for loop"
# lets say we have a list of friends names and we want to print out eah of their name in the list. you could retrive each name
# from the list individually but this would be make it repetitive with a long list of names and we would have to change our code
# each time the list lengths changed. a for loop avoids this ny letting python manage these internally
names = ['josh', 'dave', 'sarah', 'jodie']
for name in names:
    print(name)
# what I have done here is defining a list of names in variable "names" , the next line we define a for loop. this line tells python
# to pull a name from the list names and associate it with name. we then tell python to print the name that has just been assigned
# to name. python then repeats this once for each name in the list. it can be viewed as "for every name in the list of names, print the names name"

## A CLOSER LOOK AT LOOPING ##
