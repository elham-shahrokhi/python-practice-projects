# Create a dictionary to store website information with initial None values
website = {"name": None, "URL": None, "description": None, "rating": None }

# Loop through each key in the dictionary and get input from the user
for name in website.keys():
    website[name] = input(f"{name}:")

print()

# Print out the key-value pairs (user input)
for name, value in website.items():
    print(f"{name}:{value}")