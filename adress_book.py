from collections import UserDict
class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone


class AdressBook(UserDict):
    def in_data(self, name):
        if name in self.data:
            return True
        return False

    def add_record(self, record):
        self.data[record.name.value] = record

    def show_all(self):
        print(self.data)


class Record(Field):
    def __init__(self, in_name, in_phone=None):
        self.name = Name(in_name)
        self.phones = []
        if in_phone is not None:
            self.phones.append(Phone(in_phone))

    def add_phone(self, phone=None):
        if phone is not None:
            self.phones.append(Phone(phone))
        else:
            pass

    def change(self, old_note, new_note):
        for old in self.phones:
            if old.value == old_note:
                self.phones.remove(old)
                self.phones.append(Phone(new_note))

    def remove_phone(self, phone):
        for old in self.phones:
            if old.value == phone:
                self.phones.remove(old) 