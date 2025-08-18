print("🌟Contact Card🌟")
name = input("Input your name > "). capitalize()
date_of_birth = input("input your date of birth > ").strip()
telephone = input("Input your telephone number > ").strip()
email = input("Input your email > ")
address = input("Input your address > ")
contact = {"name": name, "date_of birth": date_of_birth, "telephone":telephone, "email":email, "address":address}

print()
print(f"""Name: {contact['name']}""")
print(f"""Date of birth: {contact['date_of birth']}""")
print(f"""Telephone: {contact['telephone']}""")
print(f"""Email: {contact['email']}""")
print(f"""Address: {contact['address']}""")