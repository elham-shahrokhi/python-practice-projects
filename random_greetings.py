import random

# List of different greetings in various languages
greetings = ["Hello", "Howdy", "Konnichiwa", "Guten Tag!", "Bore Da!"]

# Generate a random index between 0 and 4
index = random.randint(0, 4)

# Print a random greeting from the list
print(greetings[index])