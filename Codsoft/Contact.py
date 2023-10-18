contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    print("Contact added successfully.")

def view_contact_list():
    for index, contact in enumerate(contacts, start=1):
        print(f"Contact {index}:")
        for key, value in contact.items():
            print(f"{key}: {value}")
        print()

def search_contact():
    search_term = input("Enter the name or phone number to search for: ")
    found_contacts = []
    for contact in contacts:
        if search_term in contact["Name"] or search_term in contact["Phone"]:
            found_contacts.append(contact)
    if found_contacts:
        print("Found contacts:")
        for contact in found_contacts:
            for key, value in contact.items():
                print(f"{key}: {value}")
            print()
    else:
        print("No contacts found.")

def update_contact():
    search_term = input("Enter the name or phone number of the contact to update: ")
    for contact in contacts:
        if search_term in contact["Name"] or search_term in contact["Phone"]:
            print("Found contact. Enter new details:")
            name = input("Enter updated name: ")
            phone = input("Enter updated phone number: ")
            email = input("Enter updated email: ")
            address = input("Enter updated address: ")
            contact["Name"] = name
            contact["Phone"] = phone
            contact["Email"] = email
            contact["Address"] = address
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    search_term = input("Enter the name or phone number of the contact to delete: ")
    for contact in contacts:
        if search_term in contact["Name"] or search_term in contact["Phone"]:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

while True:
    print("Contact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact_list()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a valid option.")
