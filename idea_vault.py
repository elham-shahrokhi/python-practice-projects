import os, time, random

# function to add a new idea to the file
def add():
  os.system("clear")  # clear the screen for better UI
  idea = input("Idea > ")  # get the user's idea
  f = open("my.ideas", "a+")  # open the file in append mode (create if doesn't exist)
  f.write(f"{idea}\n")  # write the idea with a newline
  f.close()  # close the file
  time.sleep(1)
  os.system("clear")  # clear again after a short delay

# function to show a random idea from the file
def show():
  os.system("clear")  # clear screen
  f = open("my.ideas", "r")  # open the file in read mode
  ideas = f.read().split("\n")  # read and split ideas by line
  f.close()
  ideas.remove("")  # remove any empty string from the list (like last line)
  idea = random.choice(ideas)  # pick one random idea
  print(idea)  # display the idea
  time.sleep(2)
  os.system("clear")

# main loop: show menu and respond to user input
while True:
  menu = input("1: Add idea\n2: Show a random idea\n> ")
  if menu == "1":
    add()
  else:
    show()