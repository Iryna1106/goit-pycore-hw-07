from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[str(record.name)] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today()
        next_week = today + timedelta(days=7)
        current_year = today.year
        for record in self.data.values():
            try:
                birthday_this_year = record.birthday.value.replace(year=current_year)
            except AttributeError:
                continue
            if today <= birthday_this_year <= next_week:
                upcoming_birthdays.append(record)
        if upcoming_birthdays:
            result = "\n".join(
                f"{record.name}: {record.birthday.value.strftime('%d.%m.%Y')}"
                f" ({record.birthday.value.strftime('%A')}) - Birthday upcoming \U0001f389"
                for record in upcoming_birthdays
            )
            return result
        return "There are no upcoming birthdays."
