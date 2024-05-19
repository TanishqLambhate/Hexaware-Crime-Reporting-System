class Officer:
    def __init__(self, officerID, firstName, lastName, badgeNumber, rank, contactInformation, agencyID):
        self.officerID = officerID
        self.firstName = firstName
        self.lastName = lastName
        self.badgeNumber = badgeNumber
        self.rank = rank
        self.contactInformation = contactInformation
        self.agencyID = agencyID

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_badge_number(self):
        return self.badgeNumber

    def get_rank(self):
        return self.rank

    def get_contact_information(self):
        return self.contactInformation

    def get_agency_id(self):
        return self.agencyID

    # Setter methods
    def set_firstname(self, firstname):
        self.firstname = firstname

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_badge_number(self, badge_number):
        self.badgeNumber = badge_number

    def set_rank(self, rank):
        self.rank = rank

    def set_contact_information(self, contact_information):
        self.contactInformation = contact_information

    def set_agency_id(self, agency_id: int):
        self.agencyID = agency_id