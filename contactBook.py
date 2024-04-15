contacts = []

def addContact(name, phone, email, address):
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    print("************Contact added successfully!************")

def viewContacts():
    for contact in contacts:
        print(f"Name: {contact['Name']}, Phone: {contact['Phone']}")
def searchContact(searchTerm):
    foundContacts = [contact for contact in contacts
                      if searchTerm.lower() in contact['Name'].lower() or
                      searchTerm in contact['Phone']]
    for contact in foundContacts:
        print(f"Name: {contact['Name']}, Phone: {contact['Phone']}")

def updateContact(oldName, newContact):
    for i, contact in enumerate(contacts):
        if contact['Name'].lower() == oldName.lower():
            contacts[i] = newContact
            print("************Contact updated successfully!************")
            return
    print("************Contact not found.************")

def deleteContact(contactName):
    for i, contact in enumerate(contacts):
        if contact['Name'].lower() == contactName.lower():
            del contacts[i]
            print("************Contact deleted successfully!************")
            return
    print("Contact not found.")

while True:
    print("\nContact Details System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice =int( input("Enter your choice (1-6): "))
    if choice == 1:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        addContact(name, phone, email, address)
    elif choice == 2:
        print("\nContact List:")
        viewContacts()
    elif choice == 3:
        searchTerm = input("Enter Name or Phone to search: ")
        print("\nSearch Results:")
        searchContact(searchTerm)
    elif choice == 4:
        oldName = input("Enter the Name of the contact to update: ")
        name = input("Enter new Name: ")
        phone = input("Enter new Phone: ")
        email = input("Enter new Email: ")
        address = input("Enter new Address: ")
        updatedContact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        updateContact(oldName, updatedContact)

    elif choice == 5:
        contactName = input("Enter the Name of the contact to delete: ")
        deleteContact(contactName)
    elif choice == 6:
        print("Exiting Contact Details.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
