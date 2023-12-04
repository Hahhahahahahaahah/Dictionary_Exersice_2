class PhoneBook:

    def __init__(self):
        self.contactDictionary = {}
    def add_contact(self, name, phone):
        if name in self.contactDictionary:
            print("Contact already exist.")
        else:
            self.contactDictionary[name] = phone


    def lookup_contact(self, name):
        if name not in self.contactDictionary:
            print("Contact already exist.")
        else:
            print(f"{name} -> {self.contactDictionary[name]}")


    def delete_contact(self, name):
        if name not in self.contactDictionary:
            print("Contact does not exist.")
        else:
            del self.contactDictionary[name]




    def display_contacts(self):
        print("List Of Contacts")
        print("-------------------")
        for name in self.contactDictionary:
            print(f"{name} _> {self.contactDictionary[name]}")

