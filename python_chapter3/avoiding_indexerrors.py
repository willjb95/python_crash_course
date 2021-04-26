## AVOIDING INDEX ERRORS WHEN WORKING WITH LIST ##
# one type of error is common to see when working with lists for the first time which is if you ask for say item 3 but your list only has 2 items 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])
# python attempts to give you the item index 3 but when it searches for it, no item in this list has the index number. because people think 
# the third item in the index is item number 3, because they start counting at 1 but in python the first number starts at 0 

