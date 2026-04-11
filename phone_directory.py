class Contact:
    """
    A class to represent a contact in a phone directory.
    Attributes:
        name: The name of the contact.
        phone: The phone number of the contact.
        phone_directory: A class-level list that stores all Contact instances.
    Methods:
        __init__: Initialize a new contact and add to directory.
        show_contact: Return a formatted string of the contact's details.
        show_all_contacts: Display all contacts in the directory.
        search_contact: Search for a contact by name.
        validate_phone_number: Validate that a phone number is at least 8 digits.
    """
    phone_directory = []

    def __init__(self, name, phone_number):
        """
        Initialize a new Contact instance.

        Args:
            name: The name of the contact.
            phone_number: The phone number of the contact.
        """
        self.name = name
        self.phone = phone_number
        # Add this contact to the class-level phone directory
        Contact.phone_directory.append(self)

    def show_contact(self):
        """
        Returns: A string containing the contact's name and phone number.
        """
        return f"Name {self.name}, Contact number: {self.phone}"
    
    @classmethod
    def show_all_contacts(cls):
        """
        Display all contacts stored in the phone directory.
        """
        if len(cls.phone_directory) == 0:
            print("No contacts found in the directory")
        else:
            print("\nAll contacts from directory: ")
            print("=" * 60)
            for contact in cls.phone_directory:
                print(contact.show_contact())
                
    @classmethod
    def search_contact(cls, search_name):
        """
        Search for a contact by name (case-insensitive).

        Args:
            search_name: The name to search for.

        Returns:
            The phone number if found, otherwise a message indicating no contact was found.
        """
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.phone
        return f"No contact found for {search_name}"
    
    @staticmethod
    def validate_phone_number(number):
        """
        Validate that a phone number is at least 8 digits and contains only numbers.

        Args:
            number: The phone number to validate.

        Returns:
            True if valid, False otherwise.
        """
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False
        
# Get the number of contacts to add from user input
n_contacts = int(input("How many contacts do you want to add? "))
# Loop through and create contacts based on user input
for i in range(n_contacts):
    name = input("Enter the name of the contact: ")
    phone_number = input("Enter the phone number: ")
    if Contact.validate_phone_number(phone_number):
        Contact(name, phone_number)
    else:
        print(f"Invalid phone number for {name}, phone number must be atleast 8 digits and should only contain numbers.")

# Display all contacts after adding them
Contact.show_all_contacts()