## ORGANISING A LIST ##
# often your lists will be created in an unpredictable order, because you can't always control th order in which most users provide there data
# youll frequently want to present your information ina particular order. sometimes youll want to preserve the original order of your list
# and other times youll want to the original order. python provide various ways to do oragnise a list

## SORTING A LIST PERMANENTLY WITH THE SORT() METHOD ##
# pythons sort() method make it easy to sort a list, say you wanted a list in alphabetical order
cars = ['peugeot', 'vauxhall', 'honda', 'bmw']
cars.sort()
print(cars)
# so we have created a list and used the sort() method to permantantly change the order of the list, they are no in aplhabetical order and can not
# be reverted, you can also sort this list in reverse alphabetical order by passing the argument reverse=true to the sort method.
cars.sort(reverse=True)
print(cars)

## SORTING A LIST TEMPORARILY WITH THE SORTED() FUNCTION ##
# to maintain the original order of the list but present it in a sorted order you can use sorted() function, this lets you display the
# list in a particular order but doesnt affect the actuel list
print("Here is the original list in reverse")
print(cars)
print("\nHere is the the alphabaetically sorted list")
print(sorted(cars))
print("\n Here is the original list in reverse again")
print(cars)
# notice how the list still exists in its original order after we have used the sorted function
# sorting a list alphabetically is a bit more complicated when not all values are lowercase

## PRINTING A LIST IN REVERSE ORDER ##
# to reverse the orignal order of a list you can use the reverse() method, if we oringinally stored a list of drinks in order of which is our most 
# favorite, we could easily rearange the list into reverse as to have our least favorite first
drinks = ['coke', 'pepsi', 'sprite', 'monster']
print(drinks)
drinks.reverse()
print(drinks)
# notice it only reverses the order in which they were in, this changes it permanently but you can revert it by applying reverse() to the same line a second time
drinks.reverse()
print(drinks)

## FINDING THE LENGTH OF A LIST ##
# you can quickly find the length of the list by using the len() function, out previous list had four items so its length would be 4
print(len(drinks))
# this can be useful if you want to figure out the amount aliens that still need to be shot down or determine the amount of data you have to manage in a visualization



