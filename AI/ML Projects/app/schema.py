from pydantic import BaseModel


class PatientData(BaseModel):
    age: int
    gender: int
    num_procedures: int
    num_medications: int
    time_in_hospital: int