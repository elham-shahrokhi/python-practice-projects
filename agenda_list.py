# This program allows the user to manage a simple agenda list
# User can add or remove items from the list

myAgenda = []

# Function to print the current agenda list
def printList():
  print()
  for item in myAgenda:
    print(item)
  print()

# Main program loop
while True:
  menu = input("add or remove?: ")  # Ask user for action

  if menu == "add":
    item = input("What's next on the Agenda?: ")  # Get new item
    myAgenda.append(item)  # Add to agenda

  elif menu == "remove":
    item = input("What do you want to remove?: ")  # Item to remove
    if item in myAgenda:
      myAgenda.remove(item)  # Remove if exists
    else:
      print(f"{item} was not in the list")  # Handle missing item

  printList()  # Show updated agenda