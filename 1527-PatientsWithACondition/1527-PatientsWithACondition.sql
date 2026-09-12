-- Last updated: 9/12/2026, 10:21:31 AM
SELECT
    patient_id,
    patient_name,
    conditions
FROM Patients
WHERE conditions REGEXP '(^| )DIAB1';