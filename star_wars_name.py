# Simple Star Wars name generator using user input
print("STAR WARS NAME GENERATOR")

# Get all four required inputs in one line and split them into a list
all = input("Enter your first name, last name, Mum's maiden name and the city you were born in: ").split()

# Clean up each input by stripping any extra spaces
first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

# Generate the Star Wars name using slices and formatting
# First 3 letters of first name + first 3 of last name (lowercase)
# First 2 letters of maiden name + last 3 of city name (lowercase)
name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

# Print the result
print(f"Your Star Wars name is {name}")