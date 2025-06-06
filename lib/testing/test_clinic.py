import sys
import os
import pytest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Clinic, Pet, Appointment, ClinicPetVisit
from lib.base import Base

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
DATABASE_URL = "sqlite:///petcare.db"

@pytest.fixture(scope="function")
def session():
    engine = create_engine(DATABASE_URL)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_insert_clinics_and_pets(session):
    clinic = Clinic(name="Sunshine Vet", address="123 Pet St", phone="555-0000")
    pet = Pet(name="Max", species="Dog", breed="Bulldog", age=5, owner_name="Alice")

    session.add_all([clinic, pet])
    session.commit()

    assert session.query(Clinic).count() == 1
    assert session.query(Pet).count() == 1

def test_create_appointment(session):
    pet = Pet(name="Bella", species="Dog", breed="Poodle", age=3, owner_name="Bob")
    clinic = Clinic(name="Happy Paws", address="456 Animal Ave", phone="555-1111")
    session.add_all([pet, clinic])
    session.commit()

    appointment = Appointment(
        appointment_time=datetime(2025, 6, 4, 10, 30),  
        reason="Vaccination",
        pet_id=pet.id,
        clinic_id=clinic.id
    )
    session.add(appointment)
    session.commit()

    assert session.query(Appointment).count() == 1
    saved = session.query(Appointment).first()
    assert saved.reason == "Vaccination"
    assert saved.pet_id == pet.id
    assert saved.clinic_id == clinic.id

def test_clinic_pet_visit(session):
    pet = Pet(name="Charlie", species="Cat", breed="Siamese", age=2, owner_name="Carol")
    clinic = Clinic(name="Whisker Wellness", address="789 Cat Ln", phone="555-2222")
    session.add_all([pet, clinic])
    session.commit()

    visit = ClinicPetVisit(notes="Routine checkup", pet_id=pet.id, clinic_id=clinic.id)
    session.add(visit)
    session.commit()

    assert session.query(ClinicPetVisit).count() == 1
    saved = session.query(ClinicPetVisit).first()
    assert saved.notes == "Routine checkup"
    assert saved.pet_id == pet.id
    assert saved.clinic_id == clinic.id
