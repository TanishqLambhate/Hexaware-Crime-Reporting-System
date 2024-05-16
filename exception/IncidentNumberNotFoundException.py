class IncidentNumberNotFoundException(Exception):
    def __init__(self):
        super().__init__("IncidentNumberNotFound")