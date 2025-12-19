import sqlite3

class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age

class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

class Database:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()
        self.drop_tables()
        self.create_tables()

    def drop_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS patients")
        self.cursor.execute("DROP TABLE IF EXISTS doctors")

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients(
                    patient_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS doctors(
                    doctor_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    specialization TEXT 
                )
            """)

    def add_patient(self, patient_id, name, age):
        self.cursor.execute("INSERT OR IGNORE INTO patients(patient_id, name, age) VALUES (?, ?, ?)", (patient_id, name, age))

    def add_doctor(self, doctor_id, name, specialization):
        self.cursor.execute("INSERT OR IGNORE INTO doctors(doctor_id, name, specialization) VALUES (?, ?, ?)", (doctor_id, name, specialization))

    def list_senior_patients(self):
        self.cursor.execute("SELECT * FROM patients WHERE age > 65")

        rows = self.cursor.fetchall()

        #I learned about this list compreshension and argument unpacking
        senior_patients = [Patient(*row) for row in rows]

        print("Details of Senior Patients:")
        for patient in senior_patients:
            print(f"ID: {patient.patient_id}, "f"Name: {patient.name}, "f"Age: {patient.age}")

    def show_number_of_ophthalmologists(self):
        self.cursor.execute("SELECT COUNT(*) FROM doctors WHERE specialization = 'Ophthalmology'")
        number_of_opthalmologists = self.cursor.fetchone()[0]

        print("Number of opthalmologists is", number_of_opthalmologists)

if __name__ == "__main__":
    database = Database("W3A5_database_file.db")

#Adding sample data
    database.add_patient(1, "Patient1", 67)
    database.add_patient(2, "Patient2", 65)
    database.add_patient(3, "Patient3", 71)
    database.add_doctor(1, "Doctor1", "Ophthalmology")
    database.add_doctor(2, "Doctor2", "Cardiology")
    database.add_doctor(3, "Doctor3", "Ophthalmology")

#Calling methods. I put them inside database class.
    database.list_senior_patients()
    database.show_number_of_ophthalmologists()