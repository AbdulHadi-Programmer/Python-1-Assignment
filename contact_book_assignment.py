## Contact Book Management Mid Term Project :

import requests as r

# Replace Link with link variable:
SHEETY_URL = "https://api.sheety.co/link/contactBook/contact"

# POST Methods:
def add_contact(name, email, num, country, proffessionalism, notes):
    data = {
        "contact": {
            "name": name, 
            "email": email, 
            "number": num, 
            "country": country, 
            "proffession": proffessionalism, 
            "notes": notes, 
            }
        }    
    headers = {
        'Content-Type': 'application/json'
            }
    response = r.post(SHEETY_URL, json=data, headers=headers)
    return response.json()

# print(new_contact)
# print("\n\n")

# GET Method:
def read_data():
    response = r.get(SHEETY_URL)
    result = response.json()
    
    # Assuming 'result' is a dictionary with a key 'contact' that holds the list of contacts
    contacts = result.get('contact', [])

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}.")
        for key, value in contact.items():
            print(f"    {key}: {value}")
        print()


# read_data()
# print("\n\n")

# Put Method:
def update_data(id, name, email, num, country, proffessionalism, notes):
    # id = int(input("Enter the id num to update person: "))
    URL = SHEETY_URL + f"/{id}"
    response = r.get(URL)
    
    current_data = response.json().get("contact", {})
    # Prepare the data to update only the provided fields
    change_data = {
        "contact": {
            "name": name if name else current_data.get("name"),
            "email": email if email else current_data.get("email"),
            "number": num if num else current_data.get("number"),
            "country": country if country else current_data.get("country"),
            "proffession": proffessionalism if proffessionalism else current_data.get("proffession"),
            "notes": notes if notes else current_data.get("notes")
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = r.put(URL, json=change_data, headers=headers)
    print(response.json())

# update_data("Abdullah", "example@gmail.com", "0321 7845121", "Saudi Arab", "Oil Wells", "Buying and Selling Oil")

# print("\n\n")

def delete_data():
    id = int(input("Enter the id num to delete person: "))
    URL = SHEETY_URL + f"/{id}"
    response = r.delete(URL)
    if response.status_code == 204:
        print(f"Contact with id {id} successfully deleted.")
    else:
        try:
            print(response.json())
        except ValueError:
            print(f"Failed to delete contact with id {id}. Status code: {response.status_code}")    

# delete_data()

while True:
    print("\nContact Management Book using Sheety API: ")
    print("1. View All Contact \n2. Add New Contact \n3. Update Existing Contact \n4. Remove Contact \n5. Exit")
    try:
        user = int(input("Enter the Option: "))
        print("="*60)
        # Switch Case Statement:
        match user:
            case 1:
                print('\nView All Contacts: ')
                read_data()

            case 2:
                print('\nAdd New Contact: ')
                name = input('Enter name: ')
                email = input('Enter email: ')
                num = input('Enter Number: ')
                country = input('Enter Country: ')
                proffessionalism = input ("Enter the Proffession: ") 
                notes = input('Enter Specific Notes: ')

                add_contact(name, email, num, country, proffessionalism, notes)

            case 3:
                id = int(input("\nEnter the id num to update person: "))
                print('\nUpdate Existing Contact: ')
                name = input('Enter Name (If Unchanged give "" string): ')
                email = input('Enter Email (If Unchanged give "" string): ')
                num = input('Enter Number (If Unchanged give "" string): ')
                country = input('Enter Country (If Unchanged give "" string): ')
                proffessionalism = input ("Enter the Proffession (If Unchanged give "" string): ") 
                notes = input('Enter Specific Notes (If Unchanged give "" string): ')

                update_data(id, name, email, num, country, proffessionalism, notes)

            case 4:
                print("\nDelete Contact: ")
                delete_data()

            case 5:
                print('Exit...')
                break

            case _:
                print('Invalid Input')
    except Exception as e:
        print(e)
        