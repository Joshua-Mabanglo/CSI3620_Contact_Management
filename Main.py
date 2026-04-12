import Contact
from ContactBST import ContactBST

bst = ContactBST()
hash_table = ContactHashTable()

while True:
    print("\n1: Add contact")
    print("2: Search by phone")
    print("3: Search by email")
    print("4: Exit")
    print("-" * 20)

    decision = int(input("Type 1 to add, 2 to delete, 3 to exit: "))

    if(decision == 1):
        name = input("\nEnter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        
        contact = Contact.Contact(name, phone, email)
        
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



