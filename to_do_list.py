import os, time

print("To do list manager")
print()

to_do_list = []

def print_list():
    for i in to_do_list:
        print(f"{i}\n")

def add(i):
    to_do_list.append(i)
    print_list()


def remove(i):
    if exist(i):
        to_do_list.remove(i)
        print_list()
    else:
        print("this item is not in the list")



def exist(i):
    if i in to_do_list:
        return True
    else:
        return False

while True:
    work = input("Do you want to view, add, remove, delete, or edit your to do list?: ")

    if work == "add":
        item = input("What do you want to add?\n").title()
        add(item)

    elif work == "edit":
        item = input("What do you want to edit?\n").title()
        new = input("What do you want to change it to?\n").title()
        for i in range(0, len(to_do_list)):
            if to_do_list[i] == item:
                to_do_list[i] = new


    elif work == "view":
        print_list()

    elif work == "remove":
        item = input("What do you want to remove?\n").title()
        checking = input("Are you sure you want to remove this?")
        if checking[0] == "y":
            if exist(item):
                remove(item)
        else:
            print(f"{item} was not in the list")


    elif work == "delete":
        check = input("Are you sure you want to delete entire list?")
        if check[0] =="y":
            to_do_list = []
            print("the list is empty")

    else:
        print("Invalid input")

    time.sleep(1)
    #os.system('clear')



