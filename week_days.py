# Creating a program that uses a loop to ask the user
# what they thought of each of the 7 days of their last week

print("7 Days Down - What did you think?")
print()

# Loop through 7 days
for i in range(1, 8):
    # Ask the user for their thought on the day
    thought = input(f"What did you think about day {i}?\n")
    print()

    # Prepare and center-align the summary text
    myText = f"You thought day {i} was"
    print(f"{myText:^35}")  # Center-aligned heading
    print(f"{thought:^35}")  # Center-aligned response
    print()