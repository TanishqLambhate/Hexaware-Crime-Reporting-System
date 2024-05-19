# from abc import ABC, abstractmethod
# from datetime import datetime
# from ..entity.Incidents import Incident
# from ..entity.Case import Case
# from ..entity.Reports import Report

from abc import ABC, abstractmethod
from datetime import datetime
# from util.DBconn import DBConnection
class ICrimeAnalysisService(ABC):
    
    @abstractmethod
    def createIncident(self, incident):
        """
        Create a new incident
        :param incident: Incident object
        :return: Boolean
        """
        pass

    @abstractmethod
    def updateIncidentStatus(self, status, incident_id):
        """
        Update the status of an incident
        :param status: Status object
        :param incident_id: int
        :return: Boolean
        """
        pass

    @abstractmethod
    def getIncidentsInDateRange(self, start_date, end_date):
        """
        Get a list of incidents within a date range
        :param start_date: datetime
        :param end_date: datetime
        :return: Collection of Incident objects
        """
        pass

    @abstractmethod
    def searchIncidents(self, incidentID):
        """
        Search for incidents based on various criteria
        :param criteria: IncidentType object
        :return: Collection of Incident objects
        """
        pass

    @abstractmethod
    def generateIncidentReport(self, report):
        """
        Generate incident reports
        :param incident: Incident object
        :return: Report object
        """
        pass

    @abstractmethod
    def createCase(self, case_description, incidents):
        """
        Create a new case and associate it with incidents
        :param case_description: string
        :param incidents: Collection of Incident objects
        :return: Case object
        """
        pass

    @abstractmethod
    def getCaseDetails(self, case_id):
        """
        Get details of a specific case
        :param case_id: int
        :return: Case object
        """
        pass

    @abstractmethod
    def updateCaseDetails(self, case):
        """
        Update case details
        :param case: Case object
        :return: Boolean
        """
        pass

    @abstractmethod
    def getAllCases(self):
        """
        Get a list of all cases
        :return: Collection of Case objects
        """
        pass
