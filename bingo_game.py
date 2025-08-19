import random, os, time

bingo = []


# Function to generate a random number between 1 and 90
def ran():
    number = random.randint(1, 90)
    return number


# Function to display the bingo card in a formatted way
def prettyPrint():
    for row in bingo:
        for item in row:
            print(item, end="\t|\t")
        print()


# Function to create a new bingo card with random numbers
def createCard():
    global bingo
    numbers = []
    for i in range(8):
        num = ran()
        # Ensure no duplicate numbers are added
        while num in numbers:
            num = ran()
        numbers.append(ran())

    numbers.sort()  # Sort numbers to make card look neat

    # Fill the bingo card with numbers and a fixed center cell "BG"
    bingo = [[numbers[0], numbers[1], numbers[2]],
             [numbers[3], "BG", numbers[4]],
             [numbers[5], numbers[6], numbers[7]]
             ]


createCard()

# Main game loop
while True:
    prettyPrint()
    num = int(input("Next Number: "))

    # Mark the number if it's found in the bingo card
    for row in range(3):
        for item in range(3):
            if bingo[row][item] == num:
                bingo[row][item] = "X"

    # Count how many numbers have been marked
    exes = 0
    for row in bingo:
        for item in row:
            if item == "X":
                exes += 1

    # Win condition: 8 numbers marked (excluding the fixed "BG")
    if exes == 8:
        print("You have won")
        break

    time.sleep(1)
    os.system("clear")