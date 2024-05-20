import unittest
from unittest.mock import MagicMock
from dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from entity.Incidents import  Incident



class TestCrimeAnalysisService(unittest.TestCase):
    def setUp(self):
        self.service=CrimeAnalysisServiceImpl()
        # self.test_incident = Incident("Initial incidence", "2024-05-19", 23.65, 23.66, "Stolen", "Close", "3", "2")
        # self.test_incident_id = self.service.createIncident(self.test_incident)

    def test_add_incident(self):
        incidentID= 33
        incidentType= "Robbery"
        incidentDate= '2024-01-01'
        Location_Longitude= 40.71280000
        Location_Latitude= -18.24370000
        description= "Robbery occurred at the bank."
        status= "Open"
        victimID= 1
        suspectID= 2
        self.test_incident = Incident(incidentID, incidentType, incidentDate,Location_Longitude,Location_Latitude,description,status,victimID,suspectID)
        self.test_movie_id = self.service.createIncident(self.test_incident)
        self.assertIsNotNone(self.test_movie_id)

    def test_create_incident_success(self):
       
        user_input = {
            "incidentID": 32,
            "incidentType": "Robbery",
            "incidentDate": '2024-01-01',
            "Location_Longitude": 40.71280000,
            "Location_Latitude": -18.24370000,
            "description": "Robbery occurred at the bank.",
            "status": "Open",
            "victimID": 1,
            "suspectID": 2
        }

        incident = Incident(**user_input)

        service = CrimeAnalysisServiceImpl()

        success = service.createIncident(incident)

        self.assertTrue(success)
    
    def test_update_incident_status_success(self):
        
        incident_id = 1
        new_status = "Closed"
        service = CrimeAnalysisServiceImpl()

 
        success = service.updateIncidentStatus(new_status, incident_id)
        ss=service.searchIncidents(incident_id)

        self.assertTrue(success,ss)
        

if __name__ == '__main__':
    unittest.main()
