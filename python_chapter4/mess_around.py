numbers = list(range(1,31))
print(numbers)
odd_numbers = list(range(1,32,2))
print(odd_numbers)
even_number = list(range(2,31,2))
print(even_number)
three_times = list(range(3,33,3))
print(three_times)

power_three = []
for value in range(1,11):
    power_three.append(value**3)
print(power_three)
print(sum(power_three))

# nine_times = []
# for value in range(1,20):
#    nine_times.append(value*9)
# print(nine_times)
# instead of using 4 lines of code we can make it into 1 
nine_times = [value*9 for value in range(1,20)]
print(nine_times)

nine9 = list(range(0,200,9))
print(nine9)

city = ['cambridge', 'manchester', 'london', 'oxford', 'lincoln', 'liverpool']
city_been = city[0:5:2]
print("These are the cities I have visited:")
for city_beens in city_been:
    print(city_beens)
