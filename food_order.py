import os, time

# Initialize empty list to store food orders
list_of_food = []

# Function to display the current list of food orders
def pretty_print():
  os.system("clear")  # Clear the terminal
  print("list of food\n")
  counter = 1
  for order in list_of_food:
    print(f"{counter}: {order}")  # Print each order with its number
    counter += 1
  time.sleep(1)  # Pause for 1 second

# Main menu loop
while True:
  print("Yummy Food Restaurant")
  menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")

  # Add new food order
  if menu == "1":
    order = input("order > ")
    list_of_food.append(order)

  # Delete an existing food order
  elif menu == "2":
    order = input("delete order> ")
    if order in list_of_food:
      list_of_food.remove(order)

  # Show current food orders
  elif menu == "3":
    pretty_print()

  # Refresh screen after each action
  time.sleep(1)
  os.system("clear")