# Contact Book Application

contact_book = {}

def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contact_book[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added successfully!")
        
    elif choice == '2':
        name = input("Enter name to search: ")
        if name in contact_book:
            print(f"Details for {name}: Phone: {contact_book[name]['phone']}, Email: {contact_book[name]['email']}")
        else:
            print(f"Contact '{name}' not found.")
            
    elif choice == '3':
        name = input("Enter name of contact to update: ")
        if name in contact_book:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            contact_book[name] = {"phone": phone, "email": email}
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' does not exist.")
            
    elif choice == '4':
        name = input("Enter name of contact to delete: ")
        if name in contact_book:
            del contact_book[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")
            
    elif choice == '5':
        if contact_book:
            print("\n--- All Contacts ---")
            for name, details in contact_book.items():
                print(f"Name: {name} | Phone: {details['phone']} | Email: {details['email']}")
        else:
            print("Contact book is empty.")
            
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.”)
