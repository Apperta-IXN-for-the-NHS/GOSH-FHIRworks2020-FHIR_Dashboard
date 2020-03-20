from fhir_parser import FHIR, Patient, Observation
from fhir_parser.patient import Patient, Name, Telecom, Communications, Extension, Identifier
from fhir_parser.observation import Observation, ObservationComponent
import sys


class Patients:
    """
    None of the parameter or either one of them can be set as not-None
    """

    def __init__(self, page=None, patient_uuid=None):
        fhir = FHIR()
        self.uuid_presented = False
        self.patients = fhir.get_all_patients()
        if patient_uuid is not None:
            self.uuid_presented = True
            self.specific_patient = fhir.get_patient(patient_uuid)
        if page is not None:
            try:
                assert patient_uuid is None
                self.patients = fhir.get_patient_page(page)
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
            return self.specific_patient.telecoms[0].use + " " + self.specific_patient.telecoms[0].system + " " + \
                   self.specific_patient.telecoms[0].number

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


class Observations:
    def __init__(self, patients_object: Patients):
        fhir = FHIR()
        self.patients = patients_object
        self.patients_uuid_list = self.patients.get_uuid()  # List
        if type(self.patients_uuid_list) is not list:  # type is str when only patient is given
            self.patients_uuid_list = [self.patients_uuid_list]
        self.get_patient_observations_by_uuid = lambda x: fhir.get_patient_observations(x)

    """
    getter methods returns a dictionary
    result = {uuid1 : [...],
              uuid2 : [...]...  }
    Therefore, len(result) should be the same as the number of distinct patients
    """

    def get_observation_uuid(self):
        result = {}
        for uuid in self.patients_uuid_list:
            observations = self.get_patient_observations_by_uuid(uuid)
            for ob in observations:
                if uuid not in result:
                    result[uuid] = [ob.uuid]
                else:
                    result[uuid].append(ob.uuid)
        return result

    def get_type(self):
        result = {}
        for uuid in self.patients_uuid_list:
            observations = self.get_patient_observations_by_uuid(uuid)
            for ob in observations:
                if uuid not in result:
                    result[uuid] = [ob.type]
                else:
                    result[uuid].append(ob.type)
        return result

    def get_patient_uuid(self):
        result = {}
        for uuid in self.patients_uuid_list:
            observations = self.get_patient_observations_by_uuid(uuid)
            for ob in observations:
                if uuid not in result:
                    result[uuid] = [ob.patient_uuid]
                else:
                    result[uuid].append(ob.patient_uuid)
        return result

    def get_encounter_uuid(self):
        result = {}
        for uuid in self.patients_uuid_list:
            observations = self.get_patient_observations_by_uuid(uuid)
            for ob in observations:
                if uuid not in result:
                    result[uuid] = [ob.encounter_uuid]
                else:
                    result[uuid].append(ob.encounter_uuid)
        return result

    def get_datetime(self):
        result = {}
        for uuid in self.patients_uuid_list:
            observations = self.get_patient_observations_by_uuid(uuid)
            for ob in observations:
                if uuid not in result:
                    result[uuid] = [ob.issued_datetime]
                else:
                    result[uuid].append(ob.issued_datetime)
        return result

    def get_component_system(self):
        result = {}
        for uuid in self.patients_uuid_list:
            observations = self.get_patient_observations_by_uuid(uuid)
            for ob in observations:
                if uuid not in result:
                    result[uuid] = [ob.components[0].system]
                else:
                    result[uuid].append(ob.components[0].system)
        return result

    def get_component_code(self):
        result = {}
        for uuid in self.patients_uuid_list:
            observations = self.get_patient_observations_by_uuid(uuid)
            for ob in observations:
                if uuid not in result:
                    result[uuid] = [ob.components[0].code]
                else:
                    result[uuid].append(ob.components[0].code)
        return result

    def get_component_display(self):
        result = {}
        for uuid in self.patients_uuid_list:
            observations = self.get_patient_observations_by_uuid(uuid)
            for ob in observations:
                if uuid not in result:
                    result[uuid] = [ob.components[0].display]
                else:
                    result[uuid].append(ob.components[0].display)
        return result

    def get_component_quantity(self):
        result = {}
        for uuid in self.patients_uuid_list:
            observations = self.get_patient_observations_by_uuid(uuid)
            for ob in observations:
                if uuid not in result:
                    result[uuid] = [ob.components[0].quantity()]
                else:
                    result[uuid].append(ob.components[0].quantity())
        return result


# Debugging purpose main
if __name__ == "__main__":
    patient_uuid = 'b905139e-1601-403c-9d85-f8e3997cdd19'
    patient = Patients(patient_uuid=patient_uuid)
    patients = Patients(2)
    print(len(patients.get_uuid()))
    # print(patient.get_name())
    # print(patient.get_telecom())
    # print(patient.get_gender())
    # print(patient.get_birthDate())
    # print(patient.get_address())
    # print(patient.get_marital())
    # print(patient.get_language())
    observations = Observations(patients)
    # print(len(observations.get_observation_uuid()))
    # print(len(observations.get_type()))
    # print(len(observations.get_patient_uuid()))
    # print(len(observations.get_encounter_uuid()))
    # print(len(observations.get_datetime()))
    # print(len(observations.get_component_system()))
    # print(len(observations.get_component_code()))
    # print(len(observations.get_component_display()))
    # print(len(observations.get_component_quantity()))
