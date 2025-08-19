# Function to print the list in a neat table-like format
def pretty_print():
    print()
    for row in list_of_shame:
        for item in row:
            # Print each item centered in a 10-character-wide column
            print(f"{item:^10}", end=" | ")
        print()
    print()

# Initialize the main list to store user data
list_of_shame = []

while True:
    # Prompt the user to either add or remove a record
    menu = input("Add or Remove?")

    if menu.strip().lower()[0] == "a":
        # If the user selects 'a', proceed to add a new record

        name = input("What is your name? ")
        age = input("What is your age? ")
        pref = input("What is your computer platform? ")

        # Combine user inputs into a single row
        row = [name, age, pref]

        # Add the row to the main list
        list_of_shame.append(row)

    else:
        # If user selects anything other than 'a', run the remove logic

        name = input("What is the name of the record to delete?")

        # Loop through the list to find the record by name
        for row in list_of_shame:
            if name in row:
                # If a match is found, remove the entire row
                list_of_shame.remove(row)

    # Display the updated list after each action
    pretty_print()