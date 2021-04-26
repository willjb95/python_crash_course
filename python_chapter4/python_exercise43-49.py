# Q: use a for loop to print the numbers 1 - 20
num120s = list(range(1,21))
for num120 in num120s:
    print(num120)

# Q: make a list of numbers from one to one million and then use a for loop to print the numbers
one_mill = list(range(1,1_000_001))
##     for one_mills in one_mill:
##             print(one_mills) this will take a little while to complete 

# Q: make a list of numbers from one to one million, and then use min() and max() to make sure your list actaully
# starts at one and end at one million - also use the sum function to see how fast python can add a million numbers
print(min(one_mill),max(one_mill),sum(one_mill))

# Q: use the third argument of range() to make a list of odd numbers and print them out
odd_num = list(range(1,21,2))
for odd_nums in odd_num:
    print(odd_nums)

# Q: make a list of multiples of 3 from 3 to 30. use a for loop to print the numbers
odd_num2 = [value*3 for value in range(1,11)]
for odd_num2s in odd_num2:
    print(odd_num2s)

# Q: a number raised to the third power is called a cube. for example the cube of two is writtin as 2**3 in python
# make a list of the first 10 cubes and use a for loop to print out each value 
cube = []
for value in range(1,11):
    cube.append(value**3)
for cubes in cube:
    print(cubes)

# Q: use a list comprehension to generate a list of the first 10 cubes
cube = [value**3 for value in range(1,11)]
for cubes in cube:
    print(cubes)
