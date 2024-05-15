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