# This script generates a 3x3 Bingo card with a 'BINGO' center cell
import random

bingo = []  # List to store the bingo card

def ran():
    # Generate and return a random number between 1 and 90
    number = random.randint(1,90)
    return number

def pretty_print():
    # Print the bingo card row by row
    for row in bingo:
        print(row)

numbers = []  # List to hold 8 random numbers

for i in range(8):
  # Add 8 random numbers to the list
  numbers.append(ran())

numbers.sort()  # Sort the numbers in ascending order

# Create a 3x3 bingo card layout with "BINGO" in the center
bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

pretty_print()  # Display the final bingo card