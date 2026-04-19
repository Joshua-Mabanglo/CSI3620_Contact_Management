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
        for row in contactReader:
            contact = Contact.Contact(row['name'], row['phone'], row['email'])
            bst.insert(contact)
            hash_table.insert(contact)     

while True:
    print("\n1: Add contact")
    print("2: Display sorted contacts (BST)")
    print("3: Search by name (BST)")
    print("4: Delete contact")
    print("5: Update contact")
    print("6: Search by phone")
    print("7: Search by email")
    print("8: Exit")
    print("-" * 20)

    try:
        decision = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if(decision == 1):
        name = input("\nEnter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        
        contact = Contact.Contact(name, phone, email)

        toCSV = {'name': contact.name, 'phone': contact.phone, 'email': contact.email}
        
        with open('Contacts.csv', 'a', newline='') as contacts:
            contactWriter = csv.DictWriter(contacts, fieldnames=header)
            contactWriter.writerow(toCSV)
        
        print("-" * 20)
        print("Contact " + contact.name + " made.")
        
        bst.insert(contact)
        hash_table.insert(contact)
        
    elif decision == 2:
        print("\nSorted contacts (BST):")
        bst.display_sorted()  
    
    elif decision == 3:
        name = input("Enter name: ")
        result = bst.search(name)
        
        if result:
            print(f"Found: {result.name} | {result.phone} | {result.email}")
        else:
            print("No matching contact found.")
        
    elif decision == 4:
        name = input("Enter name to delete: ")
        
        # Step 1: find contact in BST
        contact = bst.search(name)
        
        if contact:
            # Step 2: remove from BST
            bst.delete(name)
            
            # Step 3: remove from hash table
            hash_table.delete(contact)
            
            # Step 4: remove from CSV
            rows = []
            
            with open('Contacts.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['name'].lower() != name.lower():
                        rows.append(row)
                        
            with open('Contacts.csv', 'w', newline='') as file:
                 writer = csv.DictWriter(file, fieldnames=['name', 'phone', 'email'])
                 writer.writeheader()
                 writer.writerows(rows)
                 
            print("Contact deleted successfully.")
            
        else:
            print("Contact not found.")
                   
    elif decision == 5:
        name = input("Enter name to update: ")
        
        # Step 1: find existing contact
        old_contact = bst.search(name)
        
        if old_contact:
            # Step 2: remove old data
            bst.delete(name)
            hash_table.delete(old_contact)
            
            # Remove from CSV
            rows = []
            with open('Contacts.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['name'].lower() != name.lower():
                        rows.append(row)
                        
            with open('Contacts.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['name', 'phone', 'email'])
                writer.writeheader()
                writer.writerows(rows)
                
            # Step 3: get new data
            print("Enter new details:")
            new_name = input("Name: ")
            new_phone = input("Phone: ")
            new_email = input("Email: ")
            
            new_contact = Contact.Contact(new_name, new_phone, new_email)
            
            # Step 4: re-add everywhere
            bst.insert(new_contact)
            hash_table.insert(new_contact)
            
            with open('Contacts.csv', 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['name', 'phone', 'email'])
                writer.writerow({
                    'name': new_contact.name,
                    'phone': new_contact.phone,
                    'email': new_contact.email
                })
                
            print("Contact update successfully.")
            
        else:
            print("Contact not found.")
        
        
        
        
    elif decision == 6:        
        phone = input("Enter phone: ")
        result = hash_table.search_by_phone(phone)

        if result:
            print(f"Found: {result.name} | {result.phone} | {result.email}")
        else:
            print("No matching contacts found.")

    elif decision == 7:
        email = input("Enter email: ")
        result = hash_table.search_by_email(email)

        if result:
            print(f"Found: {result.name} | {result.phone} | {result.email}")
        else:
            print("No matching contacts found.")

    elif decision == 8:
        print("Exiting program...")
        break

    else:
        print("Invalid option.")
