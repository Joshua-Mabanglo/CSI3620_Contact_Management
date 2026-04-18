import csv
import Contact
from ContactBST import ContactBST
from ContactHashTable import ContactHashTable

bst = ContactBST()
hash_table = ContactHashTable()

try:
    with open('Contacts.csv', 'x', newline='') as contacts:
        header = ['name','phone','email']
        contactWriter = csv.writer(contacts)
        contactWriter.writerow(header)
except FileExistsError:
    with open ('Contacts.csv', 'r') as contacts:
        contactReader = csv.DictReader(contacts)
        for contact in contactReader:
            contact = Contact.Contact(contact['name'], contact['phone'], contact['email'])
            bst.insert(contact)
            hash_table.insert(contact)      

while True:
    print("\n1: Add contact")
    print("2: Search by phone")
    print("3: Search by email")
    print("4: Exit")
    print("-" * 20)

    decision = int(input("Type 1 to add, 2 to search by phone, 3 to search by email, 4 to exit: "))

    if(decision == 1):
        name = input("\nEnter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        
        contact = Contact.Contact(name, phone, email)

        toCSV = {'name': contact.name, 'phone': contact.phone, 'email': contact.email}
        header = ['name', 'phone', 'email']
        
        with open('Contacts.csv', 'a', newline='') as contacts:
            contactWriter = csv.DictWriter(contacts, fieldnames=header)
            contactWriter.writerow(toCSV)
        
        print("-" * 20)
        print("Contact " + contact.name + " made.")
        
        bst.insert(contact)
        hash_table.insert(contact)
            
        print("\nSorted contacts (BST):")
        bst.display_sorted()
        
    
    elif decision == 2:
        phone = input("Enter phone: ")
        result = hash_table.search_by_phone(phone)

        if result:
            print("Found:", result.name, result.phone, result.email)
        else:
            print("Contact not found.")

    elif decision == 3:
        email = input("Enter email: ")
        result = hash_table.search_by_email(email)

        if result:
            print("Found:", result.name, result.phone, result.email)
        else:
            print("Contact not found.")

    elif decision == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid option.")






