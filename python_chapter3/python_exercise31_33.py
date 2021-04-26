names = ['william', 'edward', 'john', 'harriet', 'elaine']

## UPDATING THIS AFTER READING CHAPTER 4 ##
# depreciated is in GREEN
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# msg_w = f"Hello {names[0]}, I hope you are well"
# msg_e = f"Hello {names[1]}, I hope you are well"
# msg_j = f"Hello {names[2]}, I hope you are well"
# msg_h = f"Hello {names[3]}, I hope you are well"
# msg_e = f"Hello {names[4]}, I hope you are well"
# print(msg_w)
# print(msg_e)
# print(msg_j)
# print(msg_h)
# print(msg_e)

for name in names:
    print(name)
    print(f"Hello {name.title()}, I hope you are well\n")
# simplified the process of print() names and sentances using the names in the list to 3 lines of code from 15

car_brands = ['peugeot','vauxhall','honda', 'bmw']
bmw = f"I would love to own a {car_brands[-1]}!"
honda = f"I like the look of {car_brands[2]}!"
vh = f"I own a {car_brands[1]}!"
peug = f" I used to own a {car_brands[0]}!"
print(bmw, honda, vh, peug)

