import re
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not value or not re.match(r'^\d{10}$', value):
            raise ValueError("Phone number must be a 10-digit number.")
        self._value = value

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Birthday must be in the format 'YYYY-MM-DD'.")
        self._value = value

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday.value:
            today = datetime.now().date()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day).date()
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day).date()
            days_left = (next_birthday - today).days
            return days_left
        else:
            return None

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def iterator(self, page_size):
        for i in range(0, len(self.records), page_size):
            yield self.records[i:i + page_size]

