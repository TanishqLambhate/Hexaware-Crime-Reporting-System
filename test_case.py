import unittest
from unittest.mock import MagicMock
from dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from entity.Incidents import  Incident
from util.DBconn import DBConnection

from datetime import datetime


class TestCrimeAnalysisService(unittest.TestCase):
    def test_create_incident_success(self):
        # Mock user input
        user_input = {
            "incidentID": 16,
            "incidentType": "Robbery",
            "incidentDate": '2024-01-01',
            "Location_Longitude": 40.71280000,
            "Location_Latitude": -18.24370000,
            "description": "Robbery occurred at the bank.",
            "status": "Open",
            "victimID": 1,
            "suspectID": 2
        }

        # Create an Incident object
        incident = Incident(**user_input)

        # Create an instance of CrimeAnalysisServiceImpl
        service = CrimeAnalysisServiceImpl()

        # Call the createIncident method with the incident object
        success = service.createIncident(incident)

        # Assert that the method returns True (indicating successful creation)
        self.assertTrue(success)
    
    def test_update_incident_status_success(self):
        # Mock user input
        incident_id = 1
        new_status = "Closed"
        service = CrimeAnalysisServiceImpl()

        # Call the method
        success = service.updateIncidentStatus(new_status, incident_id)

        # Assertions
        self.assertTrue(success)
        

if __name__ == '__main__':
    unittest.main()
