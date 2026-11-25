class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.room = None
        self.medical_record = MedicalRecord(f"MR-{patient_id}")

    def get_details(self):
        return f"Patient {self.patient_id}: {self.name}, age {self.age}"

    def get_room_number(self):
        if self.room is None:
            return ""
        return self.room.room_number


class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

    def get_details(self):
        return f"Doctor {self.doctor_id}: {self.name} ({self.specialty})"

    def schedule_appointment(self, appointment_id, patient, date_time):
        appointment = Appointment(appointment_id, patient, self, date_time)
        return appointment


class Appointment:
    def __init__(self, appointment_id, patient, doctor, date_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time
        self.status = "scheduled"

    def complete(self):
        if self.status != "scheduled":
            return False
        self.status = "completed"
        return True

    def cancel(self):
        if self.status != "scheduled":
            return False
        self.status = "cancelled"
        return True


class HospitalRoom:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.patient = None

    def admit(self, patient):
        # Both the room and the patient must be available.
        if self.patient is not None:
            return False
        if patient.room is not None:
            return False

        self.patient = patient
        patient.room = self
        return True

    def discharge(self):
        if self.patient is None:
            return False
        self.patient.room = None
        self.patient = None
        return True


class Treatment:
    def __init__(self, treatment_id, name, cost):
        self.treatment_id = treatment_id
        self.name = name
        self.cost = cost
        self.status = "pending"

    def complete(self):
        self.status = "completed"

    def get_details(self):
        return f"Treatment {self.treatment_id}: {self.name} ({self.status}, cost {self.cost})"


class Medicine:
    def __init__(self, medicine_id, name, unit_price):
        self.medicine_id = medicine_id
        self.name = name
        self.unit_price = unit_price

    def calculate_cost(self, quantity):
        return self.unit_price * quantity

    def get_details(self):
        return f"Medicine {self.medicine_id}: {self.name} ({self.unit_price} per unit)"


class Prescription:
    def __init__(self, prescription_id, doctor, medicine, dosage, quantity):
        self.prescription_id = prescription_id
        self.doctor = doctor
        self.medicine = medicine
        self.dosage = dosage
        self.quantity = quantity

    def get_instructions(self):
        return f"{self.medicine.name}: {self.dosage} (quantity {self.quantity})"

    def calculate_cost(self):
        return self.medicine.calculate_cost(self.quantity)


class Bill:
    def __init__(self, bill_id, patient):
        self.bill_id = bill_id
        self.patient = patient
        self.charges = []

    def add_charge(self, description, amount):
        charge = {"description": description, "amount": amount}
        self.charges.append(charge)

    def calculate_total(self):
        total = 0
        for charge in self.charges:
            total = total + charge["amount"]
        return total


class LabTest:
    def __init__(self, test_id, name):
        self.test_id = test_id
        self.name = name
        self.result = None

    def record_result(self, result):
        self.result = result

    def get_details(self):
        if self.result is None:
            result = "pending"
        else:
            result = self.result
        return f"Lab test {self.test_id}: {self.name} (result: {result})"


class MedicalRecord:
    def __init__(self, record_id):
        self.record_id = record_id
        self.treatments = []
        self.lab_tests = []
        self.prescriptions = []

    def add_treatment(self, treatment_id, name, cost):
        treatment = Treatment(treatment_id, name, cost)
        self.treatments.append(treatment)
        return treatment

    def add_lab_test(self, test_id, name):
        lab_test = LabTest(test_id, name)
        self.lab_tests.append(lab_test)
        return lab_test

    def add_prescription(self, prescription_id, doctor, medicine, dosage, quantity):
        prescription = Prescription(prescription_id, doctor, medicine, dosage, quantity)
        self.prescriptions.append(prescription)
        return prescription