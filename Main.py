import Contact

print("\n1: Add contact")
print("2: Delete contact")
print("-" * 20)

decision = int(input("Type 1 to add, 2 to delete: "))

if(decision == 1):
    name = input("\nEnter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact = Contact.Contact(name, phone, email)
    print("-" * 20)
    print("Contact " + contact.name + " made.")


