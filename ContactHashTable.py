class ContactHashTable:
    def __init__(self):
        self.phone_table = {}
        self.email_table = {}

    def insert(self, contact):
        self.phone_table[contact.phone] = contact
        self.email_table[contact.email] = contact

    def search_by_phone(self, phone):
        return self.phone_table.get(phone)

    def search_by_email(self, email):
        return self.email_table.get(email)
