#Creating a program that uses a loop that asks the user what they have thought of each of the 7 days of their last week.

#For each day, prompting the user to answer a question and restate it in a full sentence that is center aligned underneath the heading.

print("7 Days Down - What did you think?")
print()
for i in range (1,8):
    thought = input(f"What did you think about day {i}?\n")
    print ()
    myText = f"You thought day {i} was"
    print(f"{myText:^35}")
    print(f"{thought:^35}")
    print()