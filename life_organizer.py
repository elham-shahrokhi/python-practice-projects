print("🌟Life Organizer🌟")

import os, time  # os for clearing the screen, time for delaying actions

# Create an empty list to store all to-do items
to_do_list = []


# Function to add a new to-do item to the list
def add():
    time.sleep(1)
    os.system("clear")

    # Get input from the user for each field of the task
    name = input("Name > ")
    date = input("Due Date > ")
    priority = input("Priority > ").capitalize()

    # Store the task data as a list of three elements
    row = [name, date, priority]

    # Append the task to the main to-do list
    to_do_list.append(row)
    print("Added")


# Function to view all tasks or filter them by priority
def view():
    time.sleep(1)
    os.system("clear")

    # Give user the option to view all tasks or filter
    options = input("1: All\n2: By Priority\n> ")

    if options == "1":
        # Loop through all tasks and print them
        for row in to_do_list:
            for item in row:
                print(item, end=" | ")
            print()
        print()
    else:
        # Filter tasks by user-defined priority
        priority = input("What priority? > ").capitalize()
        for row in to_do_list:
            if priority in row:
                for item in row:
                    print(item, end=" | ")
                print()
        print()

    time.sleep(1)


# Function to edit an existing task
def edit():
    time.sleep(1)
    os.system("clear")

    # Ask which task the user wants to edit
    find = input("Name of todo to edit > ")
    found = False

    # Check if the task exists in the list
    for row in to_do_list:
        if find in row:
            found = True

    # If not found, exit early
    if not found:
        print("Couldn't find that")
        return

    # Remove the old task before adding the updated version
    for row in to_do_list:
        if find in row:
            to_do_list.remove(row)

    # Ask for new data to replace the old task
    name = input("Name > ")
    date = input("Due Date > ")
    priority = input("Priority > ").capitalize()
    row = [name, date, priority]
    to_do_list.append(row)
    print("Added")


# Function to remove a task by name
def remove():
    time.sleep(1)
    os.system("clear")

    # Ask user for task name to remove
    find = input("Name of todo to remove > ")
    for row in to_do_list:
        if find in row:
            to_do_list.remove(row)


# Main program loop
while True:
    # Show menu options and handle user choice
    menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")

    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        edit()
    else:
        remove()

    time.sleep(1)
    os.system("clear")