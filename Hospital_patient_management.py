def search_patients(patient, disease):
    return [patient["Name"] for patient in patient if patient["Disease"] == disease]


patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = "Flu"
patients_with_disease = search_patients(patients, search_disease)

print(f"Patients with {search_disease}: {patients_with_disease}")
