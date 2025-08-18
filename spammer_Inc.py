import os, time

# Create an empty list to store email addresses
list_of_email = []

# Function to clear the screen and print all stored emails with numbering
def pretty_print():
    os.system("clear")
    print("listOfEmail")
    print()
    counter = 1
    for email in list_of_email:
        print(f"{counter}: {email}")
        counter += 1
    time.sleep(1)

# Function to simulate sending spam emails with a fun personalized message
def spam(max):
    for i in range(0, max):
        print(f"""Email {i+1}

Dear {list_of_email[i]},

We’ve been trying to reach you about... absolutely nothing important.  
But since you're on our list now, we figured — why not send you something weird?

This is your *official invitation* to do nothing, achieve nothing, and just sit there looking confused.  
If you reply to this email, we might send you a potato. Or a drawing of one. No promises.

Stay weird,  
Captain Nonsense and the Email Pirates 🏴‍☠️
""")
        time.sleep(1)
        os.system("clear")

# Main loop that shows a menu to the user and takes action based on input
while True:
    print("SPAMMER Inc.")
    menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")

    if menu == "1":
        email = input("Email > ")
        list_of_email.append(email)  # Add email to the list

    elif menu == "2":
        email = input("Email > ")
        if email in list_of_email:
            list_of_email.remove(email)  # Remove email from the list if it exists

    elif menu == "3":
        pretty_print()  # Show the list of emails

    elif menu == "4":
        spam(10)  # Simulate sending 10 spam emails

    time.sleep(1)
    os.system("clear")  # Clear screen after each operation