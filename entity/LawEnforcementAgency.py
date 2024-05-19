class LawEnforcementAgency:
    def __init__(self, agencyID, agencyName, jurisdiction, contactInformation, officers):
        self.agencyID = agencyID
        self.agencyName = agencyName
        self.jurisdiction = jurisdiction
        self.contactInformation = contactInformation
        self.officers = officers

    def get_agency_name(self):
        return self.agencyName

    def get_jurisdiction(self):
        return self.jurisdiction

    def get_contact_information(self):
        return self.contactInformation

    def get_officer(self):
        return self.officers

    
    def set_agency_name(self, agency_name):
        self.agencyName = agency_name

    def set_jurisdiction(self, jurisdiction):
        self.jurisdiction = jurisdiction

    def set_contact_information(self, contact_information):
        self.contactInformation = contact_information

    def set_officer(self, officer):
        self.officers = officer