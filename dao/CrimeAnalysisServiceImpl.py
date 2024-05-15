# from typing import Collection
from datetime import datetime
from entity.Incidents import Incident
from entity.Case import Case
from entity.Reports import Report
from dao.ICrimeAnalysisService import ICrimeAnalysisService
from datetime import datetime
from util.DBconn import DBConnection

class CrimeAnalysisServiceImpl(ICrimeAnalysisService,DBConnection):
    def createIncident(self, incident):
        # Implement logic to create a new incident
        try:
            self.cursor.execute(
                "INSERT INTO Incidents (incidentID, incidentType, incidentDate,Location_Longitude,Location_Latitude,description,status,victimID,suspectID) VALUES (?, ?, ?,?,?,?,?, ?, ?)",
                (incident.incidentID, incident.incidentType, incident.incidentDate,incident.Location_Longitude,incident.Location_Latitude,incident.description,incident.status,incident.victimID,incident.suspectID),
            )
            self.conn.commit()  # Permanent storing | If no commit then no data
        except Exception as e:
            print(e)
        print("Creating incident")
        return True

    def updateIncidentStatus(self, status, incident_id):
        # Implement logic to update the status of an incident
        self.cursor.execute(
            """
            Update Incidents
            Set status = ?
            where incidentID = ?
            """,
            (status, incident_id),
        )
        self.conn.commit()
        print(f"Updating status for incident {incident_id}")
        return True

    def getIncidentsInDateRange(self, start_date, end_date):
        # Implement logic to get incidents within a date range
        try:
            self.cursor.execute("SELECT * FROM Incidents WHERE incidentDate >= ? AND incidentDate <= ?;",(start_date,end_date))
            Incidents = self.cursor.fetchall()  # Get all data
            for Incident in Incidents:
                print(Incident)
        except Exception as e:
            print(e)

        print(f"Getting incidents from {start_date} to {end_date}")
        return []

    def searchIncidents(self, incidentID):
        # Implement logic to search for incidents based on criteria
        try:
            self.cursor.execute("Select * from Incidents where incidentId=?",(incidentID))
            Incidents = self.cursor.fetchall()  # Get all data
            # for Incident in Incidents:
            #     print(Incident)
            return Incidents
        except Exception as e:
            print(e)

        print(f"Searching incidents with criteria {incidentID}")
        return 

    def generateIncidentReport(self, report):
        # Implement logic to generate an incident report
        try:
            self.cursor.execute(
                "INSERT INTO Reports (reportID, incidentID, reportingOfficer, reportDate, reportDetails, status) VALUES (?, ?, ?,?,?,?)",
                (report.reportID, report.incidentID, report.reportingOfficer,report.reportDate,report.reportDetails,report.status),
            )
            self.conn.commit()  # Permanent storing | If no commit then no data
        except Exception as e:
            print(e)
        
        print("Generating incident report")
        return 

    def createCase(self, case_description, incidents):
        # Implement logic to create a new case and associate it with incidents
        print(f"Creating case with description: {case_description}")
        return Case()

    def getCaseDetails(self, case_id):
        # Implement logic to get details of a specific case
        print(f"Getting details for case {case_id}")
        return Case()

    def updateCaseDetails(self, case):
        # Implement logic to update case details
        print(f"Updating case details for case {case}")
        return True

    def getAllCases(self):
        # Implement logic to get a list of all cases
        print("Getting all cases")
        return []

# Example usage
# service = CrimeAnalysisServiceImpl()
# incident = Incident()
# # status = status()
# # incident_type = incident_type()

# service.createIncident(incident)
# # service.updateIncidentStatus(status, 1)
# service.getIncidentsInDateRange(datetime.now(), datetime.now())
# # service.searchIncidents(incident_type)
# service.generateIncidentReport(incident)
# service.createCase("Description", [incident])
# service.getCaseDetails(1)
# service.updateCaseDetails(Case())
# service.getAllCases()
