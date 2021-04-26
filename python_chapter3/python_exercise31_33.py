names = ['william', 'edward', 'john', 'harriet', 'elaine']
## UPDATING THIS AFTER READING CHAPTER 4 ##
# depreciated 
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
for name in names:
    print(name)

msg_w = f"Hello {names[0]}, I hope you are well"
msg_e = f"Hello {names[1]}, I hope you are well"
msg_j = f"Hello {names[2]}, I hope you are well"
msg_h = f"Hello {names[3]}, I hope you are well"
msg_e = f"Hello {names[4]}, I hope you are well"

print(msg_w)
print(msg_e)
print(msg_j)
print(msg_h)
print(msg_e)

car_brands = ['peugeot','vauxhall','honda', 'bmw']
bmw = f"I would love to own a {car_brands[-1]}!"
honda = f"I like the look of {car_brands[2]}!"
vh = f"I own a {car_brands[1]}!"
peug = f" I used to own a {car_brands[0]}!"
print(bmw, honda, vh, peug)