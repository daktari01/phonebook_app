import unittest
from phonebook import Phonebook

class TestPhonebook(unittest.TestCase):
    
    def setUp(self):
        """Initialize variables that will be used"""
        self.contact1 = Phonebook()
        
    def test_add_contact(self):
        """Test whether user can add a contact"""
        self.contact1.add_contact("John Doe", 123)
        self.assertEqual(len(self.contact1.contact_phone_list), 1)
        
    def test_update_contact(self):
        """Test whether user can update contact"""
        contact = self.contact1.update_contact("John Doe", 345)
        self.assertEqual(contact, 345)
        
    def test_view_contact(self):
        """Test whether user can view contact"""
        phone = self.contact1.contact_phone_list["John Doe"]
        self.assertEqual(phone, 345)
        
    def test_delete_contact(self):
        """Test whether user can delete contact"""
        self.contact1.delete_contact('John Doe')
        self.assertEqual(len(self.contact1.contact_phone_list), 0)
    
    if __name__ == "__main__":
        unittest.main(exit=False)