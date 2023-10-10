import pickle

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

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.records, file)

    @classmethod
    def load_from_file(cls, filename):
        address_book = cls()
        try:
            with open(filename, 'rb') as file:
                address_book.records = pickle.load(file)
        except FileNotFoundError:
            pass
        return address_book

    def search_contacts(self, search_term):
        found_contacts = []
        for record in self.records:
            if search_term in record.name or search_term in record.phone.value:
                found_contacts.append(record)
        return found_contacts

# Приклад використання:

# Створення адресної книги та додавання записів
address_book = AddressBook()
address_book.add_record(Record("John Doe", "1234567890", "1990-05-15"))
address_book.add_record(Record("Jane Smith", "9876543210", "1985-08-20"))
address_book.add_record(Record("Bob Johnson", "5555555555"))

# Збереження адресної книги на диск
address_book.save_to_file("address_book.pkl")

# Відновлення адресної книги з диска
restored_address_book = AddressBook.load_from_file("address_book.pkl")

# Пошук контактів за ім'ям або номером телефону
search_term = "John"
found_contacts = restored_address_book.search_contacts(search_term)
print("Search results for:", search_term)
for contact in found_contacts:
    print(f"Name: {contact.name}, Phone: {contact.phone.value}, Birthday: {contact.birthday.value}")
