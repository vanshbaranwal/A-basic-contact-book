#basic contact book application in python.

import json

def load_contacts(filename="contacts.json"):
    try:
        with open(filename,"r") as file:
            contacts=json.load(file)
    except FileNotFoundError:
        contacts=[]
    return contacts

def save_contact(contacts ,filename="contacts.json"):
    with open(filename,"w") as file:
        json.dump(contacts, file, indent=4)
        
def add_contact(contacts):
    name=input("enter the name : ")
    phone=input("enter the phone number : ")
    email=input("enter the email address : ")
    
    contact={
        "name": name,
        "phone": phone,
        "email": email
        }
    contacts.append(contact)
    print("contact added successfully!!!")
    
def view_contact(contacts):
    search_name=input("enter the name to search : ")
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print(f"Name: {contact['name']},Phone: {contact['phone']},Email: {contact['email']}")
            return
    print("contact not found!")
    
def search_contact(contacts):
    search_name=input("enter the name of the contact to search : ")
    for contact in contacts:
        if contact['name'].lower()==search_name.lower():
            print(f"Name: {contact['name']},Phone: {contact['phone']},Email: {contact['email']}")
            return
    print("contact not found.")
    
def update_contact(contacts):
    search_name=input("enter the name of the contact to update : ")
    for contact in contacts:
        if contact['name'].lower()==search_name.lower():
            print(f"Current Phone: {contact['phone']},Current Email {contact['email']}")
            contact["phone"]=input("enter new phone number : ")
            contact["email"]=input("enter new email : ")
            print("contact updated successfully!!")
            return
    print("contact not found.")
    
def delete_contact(contacts):
    search_name=input("enter the name of the contact to delete : ")
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            contacts.remove(contact)
            print("contact deleted successfully!!")
            return
    print("contact not found.")
    
    
def main():
    contacts=load_contacts()
    
    while True:
        print("\n_________Contact Book________")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Search contact")
        print("6. Save and exit")
        
        choice=input("choose an option ('1-6') : ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            search_contact(contacts)
        elif choice == "6":
            save_contact(contacts)
            break
        else:
            print("invalid option! please try again.")


if __name__ == "__main__":
    main()
          