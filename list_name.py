list_name =[]

def print_list():
    print()
    for name in list_name:
        print (name)
    print()

while True:
    first_name = input("first name? ").strip().capitalize()
    last_name = input ("last name? ").strip().capitalize()
    name = f"{first_name} {last_name}"
    if name not in list_name:
         list_name.append(name)
    else:
        print("ERROR: Duplicate name")
    print_list()
