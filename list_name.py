# This program stores full names in a list and avoids duplicates

list_name = []

# Function to print the current list of names
def print_list():
    print()
    for name in list_name:
        print(name)
    print()

# Main loop to collect names
while True:
    first_name = input("first name? ").strip().capitalize()  # Clean and format first name
    last_name = input("last name? ").strip().capitalize()    # Clean and format last name
    name = f"{first_name} {last_name}"  # Combine into full name

    if name not in list_name:
        list_name.append(name)  # Add to list if not duplicate
    else:
        print("ERROR: Duplicate name")  # Warn if already exists

    print_list()  # Display updated name list