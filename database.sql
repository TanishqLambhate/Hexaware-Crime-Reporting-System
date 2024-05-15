CREATE TABLE [Incidents] (
  [IncidentID] INT,
  [IncidentType] Varchar,
  [IncidentDate] Date,
  [Location] Varchar,
  [Description] Varchar,
  [Status] Varchar,
  [VictimID] INT,
  [SuspectID] INT,
  PRIMARY KEY ([IncidentID])
);

CREATE TABLE [Victims] (
  [VictimID] INT,
  [FirstName] Varchar,
  [LastName] Varchar,
  [DateOfBirth] Date,
  [Gender ] Varchar,
  [ContactInformation] Varchar,
  PRIMARY KEY ([VictimID])
);

CREATE TABLE [Suspects] (
  [SuspectID] INT,
  [FirstName] Varchar,
  [LastName] Varchar,
  [DateOfBirth] Date,
  [Gender ] Varchar,
  [ContactInformation] Varchar,
  PRIMARY KEY ([SuspectID])
);

CREATE TABLE [LawEnforcementAgencies] (
  [AgencyID] INT,
  [AgencyName] Varchar,
  [Jurisdiction] Varchar,
  [ContactInformation] Varchar,
  [Officer(s)] Varchar,
  PRIMARY KEY ([AgencyID])
);

CREATE TABLE [Officers] (
  [OfficerID] INT,
  [FirstName] Varchar,
  [LastName] Varchar,
  [BadgeNumber] INT,
  [Rank] Varchar,
  [ContactInformation] Varchar,
  [AgencyID] INT,
  PRIMARY KEY ([OfficerID])
);

CREATE TABLE [Reports] (
  [ReportID] INT,
  [IncidentID] Varchar,
  [ReportingOfficer] Varchar,
  [ReportDate] INT,
  [ReportDetails] Varchar,
  [Status] Varchar,
  PRIMARY KEY ([ReportID])
);

CREATE TABLE [Evidence] (
  [EvidenceID] INT,
  [Description] Varchar,
  [LocationFound] Varchar,
  [IncidentID] Type,
  PRIMARY KEY ([EvidenceID])
);

