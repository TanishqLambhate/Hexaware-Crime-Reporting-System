# from typing import Collection
from datetime import datetime
from entity.Incidents import Incident
from entity.Case import Case
from entity.Reports import Report
from dao.ICrimeAnalysisService import ICrimeAnalysisService
from datetime import datetime
from util.DBconn import DBConnection
from exception.IncidentNumberNotFoundException import IncidentNumberNotFoundException

class CrimeAnalysisServiceImpl(ICrimeAnalysisService,DBConnection):
    def createIncident(self, incident):
        try:
            self.cursor.execute(
                "INSERT INTO Incidents (incidentID, incidentType, incidentDate,Location_Longitude,Location_Latitude,description,status,victimID,suspectID) VALUES (?, ?, ?,?,?,?,?, ?, ?)",
                (incident.incidentID, incident.incidentType, incident.incidentDate,incident.Location_Longitude,incident.Location_Latitude,incident.description,incident.status,incident.victimID,incident.suspectID),
            )
            self.conn.commit()  
        except Exception as e:
            print(e)
        print("Creating incident")
        return True
    

    def updateIncidentStatus(self, status, incident_id):
        try:
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
        except IncidentNumberNotFoundException as I:
            print(I)
        except Exception as e:
            print(e)


    
       

    def getIncidentsInDateRange(self, start_date, end_date):
        
        try:
            self.cursor.execute("SELECT * FROM Incidents WHERE incidentDate >= ? AND incidentDate <= ?;",(start_date,end_date))
            Incidents = self.cursor.fetchall()  
            for Incident in Incidents:
                print(Incident)
        except Exception as e:
            print(e)

        print(f"Getting incidents from {start_date} to {end_date}")
        return []

    def searchIncidents(self, incidentID):
       
        try:
            self.cursor.execute("Select * from Incidents where incidentId=?",(incidentID))
            Incidents = self.cursor.fetchall()  
            return Incidents
        except Exception as e:
            print(e)

        print(f"Searching incidents with criteria {incidentID}")
        return 

    def generateIncidentReport(self, report):
      
        try:
            self.cursor.execute(
                "INSERT INTO Reports (reportID, incidentID, reportingOfficer, reportDate, reportDetails, status) VALUES (?, ?, ?,?,?,?)",
                (report.reportID, report.incidentID, report.reportingOfficer,report.reportDate,report.reportDetails,report.status),
            )
            self.conn.commit()   
        except Exception as e:
            print(e)
        
        print("Generating incident report")
        return 

    def createCase(self, caseID, case_description, incidents):

        try:
            incident_ids = [incident[0][0] for incident in incidents]
            # print("*****",incident_ids)
            incident_ids_str = ','.join(map(str, incident_ids))
            self.cursor.execute(
                "INSERT INTO [Case] (caseID, caseDescription, incidentIDs) VALUES (?, ?, ?)",
                (caseID, case_description, incident_ids_str),
            )
            self.conn.commit()  #
            print(f"Case created with ID: {caseID} and associated incidents.")
            return caseID
        except Exception as e:
            print("Failed to create case:", e)
            return None

    def getCaseDetails(self, case_id):
        try:
            self.cursor.execute("Select * from [Case] where caseID=?",(case_id))
            Cases = self.cursor.fetchall() 
            return Cases
        except Exception as e:
            print(e)
        print(f"Getting details for case {case_id}")
        return Case()

    def updateCaseDetails(self, case):
        self.cursor.execute(
            """
            Update [Case]
            Set caseDescription = ?
            where caseID = ?
            """,
            (case.caseDescription, case.caseID),
        )
        self.conn.commit()
        print(f"Updating case details for case {case}")
        return True

    def getAllCases(self):
        try:
            self.cursor.execute("Select * from [Case] ")
            Cases = self.cursor.fetchall()  
            return Cases
        except Exception as e:
            print(e)
        print("Getting all cases")
        return []

