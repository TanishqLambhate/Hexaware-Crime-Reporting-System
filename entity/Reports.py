class Report:
    def __init__(self, reportID, incidentID, reportingOfficer, reportDate, reportDetails, status):
        self.reportID = reportID
        self.incidentID = incidentID
        self.reportingOfficer = reportingOfficer
        self.reportDate = reportDate
        self.reportDetails = reportDetails
        self.status = status

    def get_incident_id(self):
        return self.incidentID

    def get_reporting_officer(self):
        return self.reportingOfficer

    def get_report_date(self):
        return self.reportDate

    def get_report_details(self):
        return self.reportDetails

    def get_status(self):
        return self.status

    # Setter methods
    def set_incident_id(self, incident_id: int):
        self.incidentID = incident_id

    def set_reporting_officer(self, reporting_officer: int):
        self.reportingOfficer = reporting_officer

    def set_report_date(self, report_date):
        self.reportDate = report_date

    def set_report_details(self, report_details):
        self.reportDetails = report_details

    def set_status(self, status):
        self.status = status