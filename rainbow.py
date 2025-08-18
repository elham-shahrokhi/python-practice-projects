# Function to change terminal text color based on the input character
def color_change(color):
    if color == "r":
        print("\033[31m", end="")  # Red
    elif color == " ":
        print("\033[0m", end="")   # Reset to default
    elif color == "b":
        print("\033[34m", end="")  # Blue
    elif color == "y":
        print("\033[33m", end="")  # Yellow
    elif color == "g":
        print("\033[32m", end="")  # Green
    elif color == "p":
        print("\033[35m", end="")  # Purple

# Ask the user for a sentence to apply rainbow coloring
sentence = input("What sentence do you want rainbow-izing?: ")

# Loop through each letter and apply color change
for letter in sentence:
    color_change(letter.lower())  # Set color based on letter
    print(letter, end="")         # Print the letter
    print()                       # Newline after each letter