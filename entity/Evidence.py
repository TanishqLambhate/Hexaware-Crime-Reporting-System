class Evidence:
    def __init__(self, evidenceID, description, locationFound, incidentID):
        self.evidenceID = evidenceID
        self.description = description
        self.locationFound = locationFound
        self.incidentID = incidentID

    def get_description(self):
        return self.description

    def get_location_found(self):
        return self.locationFound

    def get_incident_id(self):
        return self.incidentID

    def set_description(self, description: str):
        self.description = description

    def set_location_found(self, location_found: str):
        self.locationFound = location_found

    def set_incident_id(self, incident_id: int):
        self.incidentID = incident_id

    
evidence = Evidence(evidenceID=1, description="Fingerprint on doorknob", locationFound="Living Room", incidentID=101)


print("Description:", evidence.get_description())


print("Location Found:", evidence.get_location_found())
evidence.set_description("Updated description: Blood stain on carpet")
print("Updated Description:", evidence.get_description())


evidence.set_location_found("Bedroom")
print("Updated Location Found:", evidence.get_location_found())


evidence.set_incident_id(102)
print("Updated Incident ID:", evidence.get_incident_id())