from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.base import Base
from lib.models.clinic import Clinic
from lib.models.pet import Pet

DATABASE_URL = "sqlite:///petcare.db"

def reset_and_test_clinic():
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # List of clinics to add
    clinics = [
        Clinic(name="Greenfield Vet Care", address="123 Green St, Cityville", phone="555-123-4567"),
        Clinic(name="Lakeside Animal Hosp", address="456 Lake Rd, Townsville", phone="555-987-6543"),
        Clinic(name="Happy Paws Clinic", address="789 Park Ave, Villageton", phone="555-555-1212"),
    ]

    # List of pets to add
    pets = [
        Pet(name="Rex", species="Dog", breed="German Shepherd", age=4, owner_name="Dominic Kipkorir"),
        Pet(name="Bella", species="Dog", breed="Labrador", age=3, owner_name="Dominic Kipkorir"),
        Pet(name="Charlie", species="Dog", breed="Beagle", age=5, owner_name="Dominic Kipkorir"),
        Pet(name="Luna", species="Dog", breed="Golden Retriever", age=2, owner_name="Dominic Kipkorir"),
    ]

    try:
        session.add_all(clinics)
        session.add_all(pets)
        session.commit()
        print(f"Inserted {len(clinics)} clinics and {len(pets)} pets.")
    except Exception as e:
        print("Error inserting records:", e)
        session.rollback()

    # Confirm inserted records
    inserted_clinics = session.query(Clinic).all()
    inserted_pets = session.query(Pet).all()

    print("Clinics in DB:")
    for c in inserted_clinics:
        print(f" - {c.name}, {c.address}, {c.phone}")

    print("Pets in DB:")
    for p in inserted_pets:
        print(f" - {p.name}, {p.species}, {p.breed}, Age: {p.age}, Owner: {p.owner_name}")

    session.close()

if __name__ == "__main__":
    reset_and_test_clinic()
