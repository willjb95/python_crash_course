eric = "Hi Eric, Have a nice day"
print(eric)

name = "eric smith"
print(name.title())
print(name.lower())
print(name.upper())

quote = '"Tell me and I forget. Teach me and I remember. Involve me and I learn."'
author = "-Benjamin Franklin"
quote_author = f"{quote} {author}"
print(quote_author.title())

name2 = "\teric smith\n"
print("Unmodified:")
print(name2)
print("\nUsing lstrip:")
print(name2.lstrip())
print("\nUsing rstrip:")
print(name2.rstrip())
print("\nUsing strip:")
print(name2.strip())