from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.clinic import Clinic
from lib.models.pet import Pet
from lib.models.appointment import Appointment
from lib.models.clinic_pet_visit import ClinicPetVisit
 

engine = create_engine('sqlite:///petcare.db') 
Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    session.query(ClinicPetVisit).delete()
    session.query(Appointment).delete()
    session.query(Pet).delete()
    session.query(Clinic).delete()
    session.commit()


    clinics = [
        Clinic(name="Gordon-Salinas", address="36396 Larry Greens Apt. 814\nNicholemouth, AS 95592", phone="555-1234"),
        Clinic(name="Sunrise Veterinary", address="101 Main St, Springfield", phone="555-5678"),
        Clinic(name="Happy Paws Clinic", address="23 Westfield Ave, Rivertown", phone="555-9012")
    ]
    session.add_all(clinics)
    session.commit()

    pets = [
        Pet(name="Buddy", species="Dog", age=5, owner_name="Alice Johnson"),
        Pet(name="Whiskers", species="Cat", age=3, owner_name="Bob Smith"),
        Pet(name="Goldie", species="Fish", age=1, owner_name="Charlie Ray")
    ]
    session.add_all(pets)
    session.commit()


    appointments = [
        Appointment(appointment_time=datetime(2025, 6, 1, 10, 0), reason="Routine Checkup", pet_id=pets[0].id),
        Appointment(appointment_time=datetime(2025, 6, 2, 14, 30), reason="Vaccination", pet_id=pets[1].id),
        Appointment(appointment_time=datetime(2025, 6, 3, 9, 0), reason="Injury Check", pet_id=pets[2].id)
    ]
    session.add_all(appointments)
    session.commit()

   
    clinic_pet_visits = [
        ClinicPetVisit(clinic_id=clinics[0].id, pet_id=pets[0].id, visit_date=datetime(2025, 6, 1)),
        ClinicPetVisit(clinic_id=clinics[1].id, pet_id=pets[1].id, visit_date=datetime(2025, 6, 2)),
        ClinicPetVisit(clinic_id=clinics[2].id, pet_id=pets[2].id, visit_date=datetime(2025, 6, 3))
    ]
    session.add_all(clinic_pet_visits)
    session.commit()

    print(" Database seeded successfully.")

if __name__ == "__main__":
    seed_data()
