from fhir_parser import FHIR, Patient, Observation
from fhir_parser.patient import Patient, Name, Telecom, Communications, Extension, Identifier
from fhir_parser.observation import Observation, ObservationComponent
import sys

class Patients:
    """
    None of the parameter or either one of them can be set as not-None
    """

    def __init__(self, *pages, patient_uuid=None):
        fhir = FHIR()
        self.uuid_presented = False
        self.patients = fhir.get_all_patients()
        if patient_uuid is not None:
            self.uuid_presented = True
            self.specific_patient = fhir.get_patient(patient_uuid)
        if len(pages) is not 0:
            try:
                assert patient_uuid is None
                self.patients = []
                for page in pages:
                    self.patients.extend(fhir.get_patient_page(page))
            except AssertionError:
                print("Error: Can't load pages param with single patient uuid at the same time")
                sys.exit(1)

    def get_uuid(self):
        if self.uuid_presented:
            return self.specific_patient.uuid

        result = []
        for patient in self.patients:
            result.append(patient.uuid)
        return result

    def get_name(self):
        if self.uuid_presented:
            return self.specific_patient.name.prefix + " " + self.specific_patient.name.given + " " + self.specific_patient.name.family

        result = []
        for patient in self.patients:
            result.append(patient.name.prefix + " " + patient.name.given + " " + patient.name.family)
        return result

    def get_telecom(self):
        if self.uuid_presented:
            return self.specific_patient.telecoms[0].use + " " + self.specific_patient.telecoms[0].system + " " + self.specific_patient.telecoms[0].number

        result = []
        for patient in self.patients:
            result.append(patient.telecoms[0].use + " " + patient.telecoms[0].system + " " + patient.telecoms[0].number)
        return result

    def get_gender(self):
        if self.uuid_presented:
            return self.specific_patient.gender

        result = []
        for patient in self.patients:
            result.append(patient.gender)
        return result

    def get_birthDate(self):
        if self.uuid_presented:
            return str(self.specific_patient.birth_date)

        result = []
        for patient in self.patients:
            result.append(str(patient.birth_date))
        return result

    def get_address(self):
        if self.uuid_presented:
            return self.specific_patient.addresses[0].full_address.replace("\n", "")

        result = []
        for patient in self.patients:
            result.append(patient.addresses[0].full_address.replace("\n", ""))
        return result

    def get_marital(self):
        if self.uuid_presented:
            return str(self.specific_patient.marital_status)

        result = []
        for patient in self.patients:
            result.append(str(patient.marital_status))
        return result

    """
    @:returns type list -> can have multiple elements
    """
    def get_language(self):
        if self.uuid_presented:
            return self.specific_patient.communications.languages

        result = []
        for patient in self.patients:
            result.extend(patient.communications.languages)
        return result

# TODO: Observations
class Observations:
    def __init__(self, *pages, patient_object, patient_uuid):
        fhir = FHIR()
        self.patient = patient_object
        self.observations = fhir.get_patient_observations(patient_uuid)
        if pages is not None:
            observations = fhir.get_patient_observations_page(patient_uuid, pages)

    def get_uuid(self):
        pass

    def get_type(self):
        pass

    def get_patient_uuid(self):
        pass

    def get_encounter_uuid(self):
        pass

    def get_datetime(self):
        pass

    """
    component.system
    component.code
    component.display
    component.quantity()
    """

    def get_component(self):
        pass


# Debugging purpose main
if __name__ == "__main__":
    patient_uuid = '8f789d0b-3145-4cf2-8504-13159edaa747'
    patient = Patients(1)
    # print(patient.get_uuid())
    # print(patient.get_name())
    # print(patient.get_telecom())
    # print(patient.get_gender())
    # print(patient.get_birthDate())
    # print(patient.get_address())
    # print(patient.get_marital())
    print(patient.get_language())
