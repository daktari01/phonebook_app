class Phonebook:
    """Phonebook class"""
    def __init__(self):
        """Initialize variables"""
        self.contact_phone_list = {}
    
    def add_contact(self, contact_name, contact_phone):
        """Method for user to add contact"""
        self.contact_phone_list[contact_name] = contact_phone
        return self.contact_phone_list
    
    def update_contact(self, contact_name, contact_phone):
        """Method for user to update contact"""
        # User updates only the phone number
        self.contact_phone_list[contact_name] = contact_phone
        return self.contact_phone_list[contact_name]
        
    def delete_contact(self, contact_name):
        """Method for user to delete contact"""
        if contact_name in self.contact_phone_list:
            del self.contact_phone_list[contact_name]
        else:
            raise KeyError
        
    
        