from datetime import datetime
from typing import Collection
from entity.Incidents import Incident
from entity.Case import Case
from entity.Reports import Report
from dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl

def main():
    service = CrimeAnalysisServiceImpl()
    
    while True:
        print("\nCrime Analysis and Reporting System")
        print("1. Create a new incident")
        print("2. Update the status of an incident")
        print("3. Get a list of incidents within a date range")
        print("4. Search for incidents based on various criteria")
        print("5. Generate incident report")
        print("6. Create a new case and associate it with incidents")
        print("7. Get details of a specific case")
        print("8. Update case details")
        print("9. Get a list of all cases")
        print("10. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Collect input for creating a new incident
            incidentID = int(input("Enter Incident ID: "))
            incidentType = input("Enter Incident Type: ")
            incidentDate = datetime.strptime(input("Enter Incident Date (YYYY-MM-DD): "), '%Y-%m-%d')
            # location = input("Enter Location: ")
            Location_Longitude = input("Enter Location Longitude: ")
            Location_Latitude = input("Enter Location Latitude: ")
            description = input("Enter Description: ")
            status = input("Enter Status: ")
            victimID = int(input("Enter Victim ID: "))
            suspectID = int(input("Enter Suspect ID: "))
            incident = Incident(incidentID, incidentType, incidentDate,Location_Longitude,Location_Latitude, description, status, victimID, suspectID)
            success = service.createIncident(incident)
            print("Incident created successfully!" if success else "Failed to create incident.")

        elif choice == '2':
            # Collect input for updating incident status
            incidentID = int(input("Enter Incident ID: "))
            status = input("Enter new Status: ")
            success = service.updateIncidentStatus(status, incidentID)
            print("Incident status updated successfully!" if success else "Failed to update incident status.")
        
        elif choice == '3':
            # Collect input for getting incidents in a date range
            startDate = datetime.strptime(input("Enter Start Date (YYYY-MM-DD): "), '%Y-%m-%d')
            endDate = datetime.strptime(input("Enter End Date (YYYY-MM-DD): "), '%Y-%m-%d')
            incidents = service.getIncidentsInDateRange(startDate, endDate)
            for incident in incidents:
                print(incident)

        elif choice == '4':
            # Collect input for searching incidents
            incidentID = input("Enter search incidentid: ")
            incidents = service.searchIncidents(incidentID)
            for incident in incidents:
                print(incident)

        elif choice == '5':
            # Collect input for generating incident report
            incidentID = int(input("Enter Incident ID: "))
            incident = service.searchIncidents(incidentID)
            if incident:
                reportID = int(input("Enter Report ID: "))
                # incidentID = int(input("Enter Incident ID: "))
                reportingOfficer = input("Enter Reporting officer Id: ")
                reportDate = datetime.strptime(input("Enter Report Date (YYYY-MM-DD): "), '%Y-%m-%d')
                reportDetails = input("Enter Report Details: ")
                status = input("Enter Status : ")
                report = Report(reportID, incidentID, reportingOfficer, reportDate, reportDetails, status)
                success = service.generateIncidentReport(report)
                print("report created")
                print(success)
            else:
                print("Incident not found.")

        elif choice == '6':
            # Collect input for creating a new case
            caseID = int(input("Enter Case ID: "))
            caseDescription = input("Enter Case Description: ")
            incidentIDs = input("Enter Incident IDs (comma separated): ").split(',')
            incidents = [service.searchIncidents(int(incidentID)) for incidentID in incidentIDs]
            # Filter out incidents that were not found
            incidents = [incident for incident in incidents if incident]
            print(incidents)
            # Check if there are valid incidents
            if incidents:
                createdCase = service.createCase(caseID, caseDescription, incidents)
                if createdCase is not None:
                    print("Case created successfully!")
                else:
                    print("Failed to create case.")
            else:
                print("No valid incidents found.")
                
        elif choice == '7':
            # Collect input for getting case details
            caseID = int(input("Enter Case ID: "))
            case = service.getCaseDetails(caseID)
            print(case if case else "Case not found.")

        elif choice == '8':
            # Collect input for updating case details
            caseID = int(input("Enter Case ID: "))
            case = service.getCaseDetails(caseID)
            if case:
                caseDescription = input("Enter new Case Description: ")
                # incidentIDs = input("Enter Incident IDs (comma separated): ").split(',')
                # incidents = [service.searchIncidents(int(incidentID)) for incidentID in incidentIDs if service.searchIncidents(int(incidentID))]
                # case = Case(caseID, caseDescription, incidents)
                # case.caseDescription = caseDescription
                # print(case.caseDescription)
                success = service.updateCaseDetails(caseID,caseDescription)
                print("Case updated successfully!" if success else "Failed to update case.")
            else:
                print("Case not found.")

        elif choice == '9':
            # Get all cases
            cases = service.getAllCases()
            for case in cases:
                print(case)

        elif choice == '10':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
