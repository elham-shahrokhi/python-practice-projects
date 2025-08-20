import os, time, random  # Import necessary libraries

# Define a dictionary of characters and their stats
trumps = {}
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}

# Start an infinite game loop
while True:
    print("TOP TRUMPS")
    print("\nCharacters\n")

    # Display available characters
    for key in trumps:
        print(key)

    # Let the user choose a character
    user = input("Pick your character\n> ")

    # Randomly select a character for the computer
    comp = random.choice(list(trumps.keys()))
    print("Computer has picked", comp)

    # Ask user to choose a stat to compete on
    print("Choose your stat: Intelligence, Speed, Guile & Baldness Level")
    answer = input("> ")

    # Show the chosen stat for both player and computer
    print(f"{user}: {trumps[user][answer]}")
    print(f"{comp}: {trumps[comp][answer]}")

    # Compare the stat values and determine the winner
    if trumps[user][answer] > trumps[comp][answer]:
        print(user, "wins")
    elif trumps[user][answer] < trumps[comp][answer]:
        print(comp, "wins")
    else:
        print("Draw")

    # Pause and clear screen for next round
    time.sleep(2)
    os.system("clear")