import os, time

# Display title
print("To do list manager")
print()

# Create an empty list to store to-do items
to_do_list = []

# Function to print the current list
def print_list():
    for i in to_do_list:
        print(f"{i}\n")

# Function to add a new item to the list
def add(i):
    to_do_list.append(i)
    print_list()

# Function to remove an item if it exists
def remove(i):
    if exist(i):
        to_do_list.remove(i)
        print_list()
    else:
        print("this item is not in the list")

# Function to check if an item exists in the list
def exist(i):
    if i in to_do_list:
        return True
    else:
        return False

# Main program loop
while True:
    # Ask user what they want to do
    work = input("Do you want to view, add, remove, delete, or edit your to do list?: ")

    # Add new item
    if work == "add":
        item = input("What do you want to add?\n").title()
        add(item)

    # Edit an existing item
    elif work == "edit":
        item = input("What do you want to edit?\n").title()
        new = input("What do you want to change it to?\n").title()
        for i in range(0, len(to_do_list)):
            if to_do_list[i] == item:
                to_do_list[i] = new

    # View the current to-do list
    elif work == "view":
        print_list()

    # Remove a specific item
    elif work == "remove":
        item = input("What do you want to remove?\n").title()
        checking = input("Are you sure you want to remove this?")
        if checking[0] == "y":
            if exist(item):
                remove(item)
        else:
            print(f"{item} was not in the list")

    # Delete the entire list
    elif work == "delete":
        check = input("Are you sure you want to delete entire list?")
        if check[0] =="y":
            to_do_list = []
            print("the list is empty")

    # If the command is invalid
    else:
        print("Invalid input")

    # Wait 1 second before clearing or continuing
    time.sleep(1)
    # os.system('clear')  # (optional) clear the screen between each action