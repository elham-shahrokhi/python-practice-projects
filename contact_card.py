# Display a title for the contact card program
print("🌟Contact Card🌟")

# Collect user details with formatting
name = input("Input your name > ").capitalize()               # Capitalize the name
date_of_birth = input("input your date of birth > ").strip() # Remove extra spaces
telephone = input("Input your telephone number > ").strip()  # Remove extra spaces
email = input("Input your email > ")
address = input("Input your address > ")

# Store all collected data in a dictionary
contact = {
    "name": name,
    "date_of birth": date_of_birth,
    "telephone": telephone,
    "email": email,
    "address": address
}

# Display the contact details
print()
print(f"""Name: {contact['name']}""")
print(f"""Date of birth: {contact['date_of birth']}""")
print(f"""Telephone: {contact['telephone']}""")
print(f"""Email: {contact['email']}""")
print(f"""Address: {contact['address']}""")