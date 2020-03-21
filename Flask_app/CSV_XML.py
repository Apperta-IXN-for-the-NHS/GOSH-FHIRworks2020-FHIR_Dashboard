import numpy as np
import pandas as pd
from data_Model import Patients, Observations

class Process_CSV_XML:

    """
    input **kwargs format
    {
    init_patients_page=None, init_patient_uuid=None,
    patient_uuid=True, name=True, telecom=True, gender=True, birthdate=True, address=True, marital=True, language=True,
    obs_uuid=True, obs_type=True, obs_encounter_uuid=True, obs_datetime=True, obs_component_sys=True,
    obs_component_code=True, obs_component_display=True, obs_component_quantity=True
    }
    """

    def __init__(self, **kwargs):
        self.patients_object = Patients(page=kwargs["init_patients_page"] if "init_patients_page" in kwargs else None,
                                        patient_uuid=kwargs["init_patient_uuid"] if "init_patient_uuid" in kwargs else None)
        self.observations_object = Observations(self.patients_object)
        self.fields = kwargs

    def create_dataframe(self) -> pd.DataFrame:
        selected_patient_info = {}
        selected_obs_info = {}
        """
        Patients
        """
        if "patient_uuid" in self.fields and self.fields["patient_uuid"]:
            patient_uuid = np.array(self.patients_object.get_uuid())
            selected_patient_info.update({"patient_uuid" : patient_uuid})
            del patient_uuid

        if "name" in self.fields and self.fields["name"]:
            name = np.array(self.patients_object.get_name())
            selected_patient_info.update({"name": name})
            del name

        if "telecom" in self.fields and self.fields["telecom"]:
            telecom = np.array(self.patients_object.get_telecom())
            selected_patient_info.update({"telecom": telecom})
            del telecom

        if "gender" in self.fields and self.fields["gender"]:
            gender = np.array(self.patients_object.get_gender())
            selected_patient_info.update({"gender": gender})
            del gender

        if "birthdate" in self.fields and self.fields["birthdate"]:
            birthdate = np.array(self.patients_object.get_birthdate())
            selected_patient_info.update({"birthdate": birthdate})
            del birthdate

        if "address" in self.fields and self.fields["address"]:
            address = np.array(self.patients_object.get_address())
            selected_patient_info.update({"address": address})
            del address

        if "marital" in self.fields and self.fields["marital"]:
            marital = np.array(self.patients_object.get_marital())
            selected_patient_info.update({"marital": marital})
            del marital

        if "language" in self.fields and self.fields["language"]:
            language = np.array(self.patients_object.get_language())
            selected_patient_info.update({"language": language})
            del language

        """
        Observations
        """
        if "obs_uuid" in self.fields and self.fields["obs_uuid"]:
            obs_uuid = self.observations_object.get_observation_uuid()
            selected_obs_info.update(obs_uuid)
            del obs_uuid

        if "obs_type" in self.fields and self.fields["obs_type"]:
            obs_type = self.observations_object.get_type()
            selected_obs_info.update(obs_type)
            del obs_type

        if "obs_encounter_uuid" in self.fields and self.fields["obs_encounter_uuid"]:
            obs_encounter_uuid = self.observations_object.get_encounter_uuid()
            selected_obs_info.update(obs_encounter_uuid)
            del obs_encounter_uuid

        if "obs_datetime" in self.fields and self.fields["obs_datetime"]:
            obs_datetime = self.observations_object.get_datetime()
            selected_obs_info.update(obs_datetime)
            del obs_datetime

        if "obs_component_sys" in self.fields and self.fields["obs_component_sys"]:
            obs_component_sys = self.observations_object.get_component_system()
            selected_obs_info.update(obs_component_sys)
            del obs_component_sys

        if "obs_component_code" in self.fields and self.fields["obs_component_code"]:
            obs_component_code = self.observations_object.get_component_code()
            selected_obs_info.update(obs_component_code)
            del obs_component_code

        if "obs_component_display" in self.fields and self.fields["obs_component_display"]:
            obs_component_display = self.observations_object.get_component_display()
            selected_obs_info.update(obs_component_display)
            del obs_component_display

        if "obs_component_quantity" in self.fields and self.fields["obs_component_quantity"]:
            obs_component_quantity = self.observations_object.get_component_quantity()
            selected_obs_info.update(obs_component_quantity)
            del obs_component_quantity

        columns = [*selected_patient_info]
        columns.extend([*selected_obs_info])

        # df = pd.DataFrame(selected_obs_info)

        # return selected_obs_info
        # TODO: How are you going to deal with foreign keys and different length? how are you going to loop
        for uuid in selected_obs_info.keys():
            print(len(selected_obs_info[uuid]))

    def generate_csv(self):
        pass

    def df_to_xml(self, filepath):
        pass

    def generate_xml(self):
        pass

if __name__ == "__main__":
    init_patient_uuid = 'b905139e-1601-403c-9d85-f8e3997cdd19'
    csvxml = Process_CSV_XML(init_patients_page=1, patient_uuid=True, name=True, address=True, marital=True, obs_uuid=True, obs_type=False)
    print(csvxml.create_dataframe())
