import matplotlib.pyplot as plt
from fhir_parser import FHIR

fhir = FHIR()
patients = fhir.get_all_patients()


def getLanguage():
    languages = {}
    for patient in patients:
        for language in patient.communications.languages:
            languages.update({language: languages.get(language, 0) + 1})

    return languages

def getMarital():
    marital_status = {}
    for patient in patients:
        if str(patient.marital_status) in marital_status:
            marital_status[str(patient.marital_status)] += 1
        else:
            marital_status[str(patient.marital_status)] = 1

    return marital_status

def getAverageAge():
    ages = []
    for patient in patients:
        ages.append(patient.age())

    return sum(ages) / len(ages)

def getYoungestAge():
    youngest = 1000
    for patient in patients:
        if patient.age() < youngest:
            youngest = patient.age()

    return youngest

def getOldestAge():
    oldest = -1
    for patient in patients:
        if patient.age() > oldest:
            oldest = patient.age()

    return oldest

def graphLanguage():
    pass

def graphMarital():
    pass

def graphAge():
    pass