class Contacts:
    def __init__(self, name, phone_number):
        self.name=name
        self.phone_number=phone_number
    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number)== 10:
            return True
        else:
            False

class ContactList:
    all_contacts = []
    
    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contacts.validate_phone_number(phone_number):
            raise ValueError ('Неверное количество символов')
        new_contact=Contacts(name, phone_number)
        cls.all_contacts += [new_contact]
        return new_contact
               
print(ContactList.all_contacts)       
ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")
# ContactList.add_contact("John Doe", "5551234")
for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)
  


        

