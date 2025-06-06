# lib/cli.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.base import SessionLocal
from lib.models import Clinic, Pet, Appointment, ClinicPetVisit
from datetime import datetime


def main():
    print("Welcome to PetCare Manager CLI!")
    session = SessionLocal()

    while True:
        print_main_menu()
        choice = input("> ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            clinic_menu(session)
        elif choice == "2":
            pet_menu(session)
        elif choice == "3":
            appointment_menu(session)
        elif choice == "4":
            clinic_pet_visit_menu(session)
        else:
            print("Invalid choice, please try again.")

    session.close()


def print_main_menu():
    print("\nMain Menu:")
    print("1. Manage Clinics")
    print("2. Manage Pets")
    print("3. Manage Appointments")
    print("4. Manage Clinic Pet Visits")
    print("0. Exit")


# Clinic Menu and functions

def clinic_menu(session):
    while True:
        print("\nClinic Menu:")
        print("1. Create Clinic")
        print("2. Delete Clinic")
        print("3. List all Clinics")
        print("4. Find Clinic by Name")
        print("5. View Clinic's Pet Visits")
        print("0. Back to Main Menu")

        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            create_clinic(session)
        elif choice == "2":
            delete_clinic(session)
        elif choice == "3":
            list_clinics(session)
        elif choice == "4":
            find_clinic_by_name(session)
        elif choice == "5":
            view_clinic_pet_visits(session)
        else:
            print("Invalid choice, try again.")


def create_clinic(session):
    try:
        name = input("Enter clinic name: ").strip()
        address = input("Enter clinic address: ").strip()
        phone = input("Enter clinic phone: ").strip()
        clinic = Clinic(name=name, address=address, phone=phone)
        clinic.save(session)
        print(f"Clinic '{name}' created successfully.")
    except Exception as e:
        print(f"Error creating clinic: {e}")


def delete_clinic(session):
    try:
        list_clinics(session)
        cid = int(input("Enter Clinic ID to delete: "))
        clinic = Clinic.find_by_id(session, cid)
        if clinic:
            clinic.delete(session)
            print(f"Clinic with ID {cid} deleted.")
        else:
            print("Clinic not found.")
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")
    except Exception as e:
        print(f"Error deleting clinic: {e}")


def list_clinics(session):
    clinics = Clinic.get_all(session)
    if clinics:
        print("Clinics:")
        for c in clinics:
            print(f"ID: {c.id} | Name: {c.name} | Address: {c.address} | Phone: {c.phone}")
    else:
        print("No clinics found.")


def find_clinic_by_name(session):
    name = input("Enter clinic name to search: ").strip()
    clinics = Clinic.find_by_attribute(session, 'name', name)
    if clinics:
        for c in clinics:
            print(f"ID: {c.id} | Name: {c.name} | Address: {c.address} | Phone: {c.phone}")
    else:
        print("No clinics found with that name.")


def view_clinic_pet_visits(session):
    try:
        list_clinics(session)
        cid = int(input("Enter Clinic ID to view pet visits: "))
        clinic = Clinic.find_by_id(session, cid)
        if clinic:
            visits = clinic.pet_visits
            if visits:
                print(f"Pet visits for clinic '{clinic.name}':")
                for visit in visits:
                    pet = visit.pet
                    print(f"Visit ID: {visit.id}, Pet: {pet.name} (ID: {pet.id}), Visit Date: {visit.visit_date}")
            else:
                print("No pet visits found for this clinic.")
        else:
            print("Clinic not found.")
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")


# Pet Menu and functions

def pet_menu(session):
    while True:
        print("\nPet Menu:")
        print("1. Create Pet")
        print("2. Delete Pet")
        print("3. List all Pets")
        print("4. Find Pet by Name")
        print("0. Back to Main Menu")

        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            create_pet(session)
        elif choice == "2":
            delete_pet(session)
        elif choice == "3":
            list_pets(session)
        elif choice == "4":
            find_pet_by_name(session)
        else:
            print("Invalid choice, try again.")


def create_pet(session):
    try:
        name = input("Enter pet name: ").strip()
        species = input("Enter pet species: ").strip()
        breed = input("Enter pet breed: ").strip()
        age = int(input("Enter pet age (years): "))
        owner_name = input("Enter owner name: ")
        pet = Pet(name=name, species=species, breed=breed, age=age, owner_name=owner_name)
        pet.save(session)
        print(f"Pet '{name}' created successfully.")
    except ValueError:
        print("Invalid age input. Please enter an integer.")
    except Exception as e:
        print(f"Error creating pet: {e}")


def delete_pet(session):
    try:
        list_pets(session)
        pid = int(input("Enter Pet ID to delete: "))
        pet = Pet.find_by_id(session, pid)
        if pet:
            pet.delete(session)
            print(f"Pet with ID {pid} deleted.")
        else:
            print("Pet not found.")
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")
    except Exception as e:
        print(f"Error deleting pet: {e}")


def list_pets(session):
    pets = Pet.get_all(session)
    if pets:
        print("Pets:")
        for p in pets:
            print(f"ID: {p.id} | Name: {p.name} | Species: {p.species} | Breed: {p.breed} | Age: {p.age}")
    else:
        print("No pets found.")


def find_pet_by_name(session):
    name = input("Enter pet name to search: ").strip()
    pets = Pet.find_by_attribute(session, 'name', name)
    if pets:
        for p in pets:
            print(f"ID: {p.id} | Name: {p.name} | Species: {p.species} | Breed: {p.breed} | Age: {p.age}")
    else:
        print("No pets found with that name.")


# Appointment Menu and functions

def appointment_menu(session):
    while True:
        print("\nAppointment Menu:")
        print("1. Create Appointment")
        print("2. Delete Appointment")
        print("3. List all Appointments")
        print("4. Find Appointment by Pet ID")
        print("0. Back to Main Menu")

        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            create_appointment(session)
        elif choice == "2":
            delete_appointment(session)
        elif choice == "3":
            list_appointments(session)
        elif choice == "4":
            find_appointment_by_pet_id(session)
        else:
            print("Invalid choice, try again.")


def create_appointment(session):
    try:
        pet_id = int(input("Enter Pet ID for the appointment: "))
        date_input = input("Enter appointment date (YYYY-MM-DD): ").strip()
        reason = input("Enter reason for appointment: ").strip()

        pet = Pet.find_by_id(session, pet_id)
        if not pet:
            print("Pet not found.")
            return

        appointment_datetime = datetime.strptime(date_input, "%Y-%m-%d")

        appointment = Appointment(
            pet_id=pet_id,
            appointment_time=appointment_datetime, 
            reason=reason
        )

        session.add(appointment)
        session.commit()

        print(f"Appointment created for pet '{pet.name}' on {appointment_datetime.date()}.")
    except ValueError:
        print("Invalid input. Please ensure IDs are integers and date format is YYYY-MM-DD.")
    except Exception as e:
        print(f"Error creating appointment: {e}")


def delete_appointment(session):
    try:
        list_appointments(session)
        aid = int(input("Enter Appointment ID to delete: "))
        appointment = Appointment.find_by_id(session, aid)
        if appointment:
            appointment.delete(session)
            print(f"Appointment with ID {aid} deleted.")
        else:
            print("Appointment not found.")
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")
    except Exception as e:
        print(f"Error deleting appointment: {e}")


def list_appointments(session):
    appointments = Appointment.get_all(session)
    if appointments:
        print("Appointments:")
        for a in appointments:
            pet = a.pet
            appt_time = a.appointment_time.strftime("%Y-%m-%d") if a.appointment_time else "N/A"
            print(f"ID: {a.id} | Pet: {pet.name if pet else 'Unknown'} (ID: {a.pet_id}) | Date: {appt_time} | Reason: {a.reason}")
    else:
        print("No appointments found.")


def find_appointment_by_pet_id(session):
    try:
        pet_id = int(input("Enter Pet ID to find appointments: "))
        appointments = Appointment.find_by_attribute(session, 'pet_id', pet_id)
        if appointments:
            for a in appointments:
                appt_time = a.appointment_time.strftime("%Y-%m-%d") if a.appointment_time else "N/A"
                print(f"ID: {a.id} | Date: {appt_time} | Reason: {a.reason}")
        else:
            print("No appointments found for that pet.")
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")


# Clinic Pet Visit Menu and functions

def clinic_pet_visit_menu(session):
    while True:
        print("\nClinic Pet Visit Menu:")
        print("1. Create Clinic Pet Visit")
        print("2. Delete Clinic Pet Visit")
        print("3. List all Clinic Pet Visits")
        print("4. Find Clinic Pet Visit by Pet ID")
        print("0. Back to Main Menu")

        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            create_clinic_pet_visit(session)
        elif choice == "2":
            delete_clinic_pet_visit(session)
        elif choice == "3":
            list_clinic_pet_visits(session)
        elif choice == "4":
            find_clinic_pet_visit_by_pet_id(session)
        else:
            print("Invalid choice, try again.")


def create_clinic_pet_visit(session):
    try:
        list_clinics(session)
        clinic_id = int(input("Enter Clinic ID for the visit: "))
        clinic = Clinic.find_by_id(session, clinic_id)
        if not clinic:
            print("Clinic not found.")
            return

        list_pets(session)
        pet_id = int(input("Enter Pet ID for the visit: "))
        pet = Pet.find_by_id(session, pet_id)
        if not pet:
            print("Pet not found.")
            return

        visit_date_input = input("Enter visit date (YYYY-MM-DD): ").strip()
        visit_date = datetime.strptime(visit_date_input, "%Y-%m-%d").date()

        clinic_pet_visit = ClinicPetVisit(
            clinic_id=clinic_id,
            pet_id=pet_id,
            visit_date=visit_date,
        )
        session.add(clinic_pet_visit)
        session.commit()

        print(f"Clinic Pet Visit created for pet '{pet.name}' at clinic '{clinic.name}' on {visit_date}.")
    except ValueError:
        print("Invalid input. Please ensure IDs are integers and date is in YYYY-MM-DD format.")
    except Exception as e:
        print(f"Error creating clinic pet visit: {e}")


def delete_clinic_pet_visit(session):
    try:
        list_clinic_pet_visits(session)
        cpid = int(input("Enter Clinic Pet Visit ID to delete: "))
        visit = ClinicPetVisit.find_by_id(session, cpid)
        if visit:
            visit.delete(session)
            print(f"Clinic Pet Visit with ID {cpid} deleted.")
        else:
            print("Clinic Pet Visit not found.")
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")
    except Exception as e:
        print(f"Error deleting clinic pet visit: {e}")


def list_clinic_pet_visits(session):
    visits = ClinicPetVisit.get_all(session)
    if visits:
        print("Clinic Pet Visits:")
        for v in visits:
            print(f"ID: {v.id} | Clinic: {v.clinic.name if v.clinic else 'Unknown'} | Pet: {v.pet.name if v.pet else 'Unknown'} | Visit Date: {v.visit_date}")
    else:
        print("No clinic pet visits found.")


def find_clinic_pet_visit_by_pet_id(session):
    try:
        pet_id = int(input("Enter Pet ID to find clinic pet visits: "))
        visits = ClinicPetVisit.find_by_attribute(session, 'pet_id', pet_id)
        if visits:
            for v in visits:
                print(f"ID: {v.id} | Clinic: {v.clinic.name if v.clinic else 'Unknown'} | Visit Date: {v.visit_date}")
        else:
            print("No clinic pet visits found for that pet.")
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")


if __name__ == "__main__":
    main()
