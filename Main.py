import Contact
from ContactBST import ContactBST

bst = ContactBST()

while True:
    print("\n1: Add contact")
    print("2: Delete contact")
    print("3: Exit")
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
            
        print("\nSorted contacts (BST):")
        bst.display_sorted()
        
    elif(decision == 2):
        print("Delete not implemented yet.")
        
    elif decision == 3:
        print("Exiting program...")
        break 
        




