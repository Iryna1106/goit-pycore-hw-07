from functions.functions_record import (
    add_contact, change_contact, show_phone, show_all, delete_contact
)
from functions.functions_bday import add_birthday, show_birthday, birthdays
from addressbook.addressbook import AddressBook
from utils.utils import parse_input


def main():
    book = AddressBook()
    print("Welcome to an assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("See you!")
                break
            elif command == "hello":
                print("What would you like me to do?")
            elif command == "add":
                print(add_contact(args, book))
            elif command == "change":
                print(change_contact(args, book))
            elif command == "phone":
                print(show_phone(args[0], book))
            elif command == "all":
                print(show_all(book))
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                print(birthdays(book))
            elif command == "delete":
                print(delete_contact(args, book))
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
