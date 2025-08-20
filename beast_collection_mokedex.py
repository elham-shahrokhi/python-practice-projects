import os, time  # Importing modules for clearing the screen and adding delay

# Dictionary to store the beasts with their name as key and attributes as values
mokedex = {}


# Function to display all the beasts in a formatted table
def prettyـprint():
    print(f"Name\tType\tHP\tMP")  # Table header
    for key, value in mokedex.items():
        # Print each beast's name, type, HP, and MP with centered alignment
        print(f"""{key:^12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")


# Infinite loop to keep collecting user input
while True:
    print("Add your Beast!")

    # Getting input from the user and formatting them properly
    name = input("Name > ").title()
    type = input("Type > ").title()
    hp = int(input("HP > "))
    mp = int(input("MP > "))

    # Saving the beast's data in the dictionary using the name as the key
    mokedex[name] = {"type": type, "hp": hp, "mp": mp}

    # Divider and printing the full list
    print("----------\n")
    prettyـprint()