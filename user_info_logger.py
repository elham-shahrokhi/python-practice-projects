# Function to print the list in a neat table-like format
def pretty_print():
    print()
    for row in list_of_shame:
        for item in row:
            # item refers to each column entry in a row
            print(f"{item:^10}", end=" | ")
            # :^10 centers the text within 10 characters; the separator is " | " to mimic a table layout
        print()
    print()

# Initialize an empty list to store user information
list_of_shame = []

while True:
    # Get user input
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")

    # Store the inputs as a row
    row = [name, age, pref]

    # Add the row to the main list
    list_of_shame.append(row)

    # Ask if the user wants to exit
    exit = input("Exit? y/n")
    if (exit.strip().lower()[0] == "y"):
        break  # Exit the loop if the user types something starting with "y"

# Print the formatted list
pretty_print()