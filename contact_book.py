contacts = {}

while True:
    print("\n1 Add Contact")
    print("2 Search Contact")
    print("3 Delete Contact")
    print("4 View Contacts")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif choice == "2":
        name = input("Enter name: ")
        print("Phone:", contacts.get(name, "Not found"))

    elif choice == "3":
        name = input("Enter name: ")
        contacts.pop(name, None)

    elif choice == "4":
        print(contacts)

    elif choice == "5":
        break
