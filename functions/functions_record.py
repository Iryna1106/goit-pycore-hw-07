from decorators.decorators import input_error
from addressbook.addressbook import AddressBook
from contacts.record import Record


@input_error
def add_contact(args, address_book: AddressBook):
    name, phone, *_ = args
    formatted_name = name.capitalize()
    record = address_book.find(formatted_name)
    message = "Contact updated."
    if record is None:
        record = Record(formatted_name)
        address_book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, address_book: AddressBook):
    if len(args) != 3:
        raise ValueError
    name, old_phone, new_phone = args
    name = name.capitalize()
    record = address_book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return f"Contact {name} updated."
    raise KeyError(f"{name} not found")


@input_error
def show_phone(name, address_book: AddressBook):
    record = address_book.find(name.capitalize())
    if record:
        phones = ', '.join(str(p) for p in record.phones)
        return f"Phone number(s) for {record.name}: {phones}"
    raise KeyError(f"{name} not found")


@input_error
def show_all(address_book: AddressBook):
    contacts = address_book.data
    if not contacts:
        return "No contacts saved."
    result = "Name    | Phone       | Birthday\n"
    result += "--------|-------------|------------------\n"
    for _, record in contacts.items():
        birthday_info = (
            record.birthday.value.strftime("%d.%m.%Y") if record.birthday else ""
        )
        result += (
            f"{record.name.value:<7} | "
            f"{', '.join(map(str, record.phones)):<11} | "
            f"{birthday_info}\n"
        )
    return result.strip()


@input_error
def delete_contact(args, address_book: AddressBook):
    if len(args) != 1:
        raise ValueError(
            "Invalid command. Please provide the name of the contact to delete."
        )
    name = args[0].capitalize()
    if name in address_book.data:
        del address_book.data[name]
        return f"Contact {name} deleted."
    raise KeyError(f"{name} not found")
