class Incident:
    def __init__(self, incidentID, incidentType, incidentDate,  Location_Longitude,Location_Latitude,description, status, victimID, suspectID):
        self.incidentID = incidentID
        self.incidentType = incidentType
        self.incidentDate = incidentDate
        # self.location = location
        self.Location_Longitude = Location_Longitude
        self.Location_Latitude = Location_Latitude
        self.description = description
        self.status = status
        self.victimID = victimID
        self.suspectID = suspectID

    def set_incident_type(self, incident_type):
        self.incidentType = incident_type

    def set_incident_date(self, incident_date):
        self.incidentDate = incident_date

    def set_location_longitude(self, location_longitude):
        self.Location_Longitude = location_longitude

    def set_location_latitude(self, location_latitude):
        self.Location_Latitude = location_latitude

    def set_description(self, description):
        self.description = description

    def set_status(self, status):
        self.status = status

    def set_victim_id(self, victim_id):
        self.victimID = victim_id

    def set_suspect_id(self, suspect_id):
        self.suspectID = suspect_id

     # Getter methods
    def get_incident_type(self):
        return self.incidentType

    def get_incident_date(self):
        return self.incidentDate

    def get_location_longitude(self):
        return self.Location_Longitude

    def get_location_latitude(self):
        return self.Location_Latitude

    def get_description(self):
        return self.description

    def get_status(self):
        return self.status

    def get_victim_id(self):
        return self.victimID

    def get_suspect_id(self):
        return self.suspectID