from PhoneBook import PhoneBook


def main():
    phone_book = PhoneBook()
    print("Welcome to Phone Book!\n")

    while True:
        print("1. Add contact")
        print("2. Lookup contact")
        print("3. Delete contact")
        print("4. Display all contacts")
        print("5. Quit")

        choice = input("\nPlease enter your choice: ")
        print()

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            print("")
            phone_book.add_contact(name, phone)

        elif choice == "2":
            name = input("Enter contact name: ")
            print("")
            phone_book.lookup_contact(name)

        elif choice == "3":
            name = input("Enter contact name to delete: ")
            print("")
            phone_book.delete_contact(name)

        elif choice == "4":
            print("Phone Book:")
            phone_book.display_contacts()

        elif choice == "5":
            print("")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")



if __name__ == "__main__":
    main()
