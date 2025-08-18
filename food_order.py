import os, time
list_of_food = []

def pretty_print():
  os.system("clear")
  print("list of food")
  print()
  counter = 1
  for order in list_of_food:
    print(f"{counter}: {order}")
    counter += 1
  time.sleep(1)
while True:
  print("Yummy Food Restaurant")
  menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
  if menu == "1":
    order = input("order > ")
    list_of_food.append(order)
  elif menu =="2":
    order = input ("delete order> ")
    if order in list_of_food:
      list_of_food.remove(order)
  elif menu == "3":
      pretty_print()
  time.sleep(1)
  os.system("clear")