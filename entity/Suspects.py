class Suspect:
    def __init__(self, suspectID, firstName, lastName, dateOfBirth, gender, contactInformation):
        self.suspectID = suspectID
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.gender = gender
        self.contactInformation = contactInformation
    
    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_date_of_birth(self):
        return self.dateOfBirth

    def get_gender(self):
        return self.gender

    def get_contact_information(self):
        return self.contactInformation

    # Setter methods
    def set_firstname(self, firstname: str):
        self.firstname = firstname

    def set_lastname(self, lastname: str):
        self.lastname = lastname

    def set_date_of_birth(self, date_of_birth):
        self.dateOfBirth = date_of_birth

    def set_gender(self, gender: str):
        self.gender = gender

    def set_contact_information(self, contact_information):
        self.contactInformation = contact_information