# I wanted to insert a variable into a string so i used an f-string which i place at the start of my msg and add each variable i want in close brace, squiggly brackets 
ed_age = 69
mental_age = 3
msg = f"Edwards physical age is {ed_age}, but is mental age is {mental_age}."
print(msg)

# I created two variables (birth year andf curretn year) to figure out my age by working out the difference between them, i used the abs function
# which is a built-in function and returns the absolute value for the given number
birth_year = 1995
current_year = 2021
age = abs(birth_year-current_year)
print(age)
