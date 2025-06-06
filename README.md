## PetCareManager
PetCareManager is a CLI-based application designed to help users manage pet care data, including clinics, pets, appointments, and pet visits. It leverages a modular Python codebase with SQLAlchemy ORM and Alembic for database migrations.
## Features
1. Pet Management
 Add a Pet: Users can register new pets by providing:

 Name

 Species (e.g., Dog, Cat)

 Breed

 Age

 Owner's Name

 View Pets: Lists all pets currently stored in the database with their details.

 Update Pet Info: Allows editing pet details if there's a change (e.g., updated owner name or age).

 Delete a Pet: Removes a pet and its associated records (like appointments and visits, if cascaded properly).

2. Clinic Management
 Add a Clinic: Register a new clinic by entering:

 Clinic Name

 Address

 Phone Number

 View Clinics: Displays all registered veterinary clinics.

 Update Clinic Info: Modify clinic name, location, or contact number.

Delete a Clinic: Removes a clinic and optionally its appointments/visits.

3. Appointment Scheduling
 Create Appointment: Link a pet to a clinic by selecting from available IDs, and provide:

 Appointment date & time

 Reason for the visit (e.g., Vaccination, Checkup)

 View Appointments: List all appointments with pet and clinic details.

 Delete Appointment: Cancel a scheduled visit

4. Clinic Pet Visit Records
 Log Visit: After an appointment or walk-in, users can log notes from a visit (e.g., diagnosis, prescriptions).

 View Visits: List past clinic visits by pet and clinic, along with visit notes.

 Delete Visit Record: Remove incorrect or outdated visit logs.

## Installation
 Clone the repository:
 git clone git@github.com:Harshpal01/petcare_manager.git
 cd petcare_manager
# Create and activate a virtual environment (recommended): 
python -m venv venv
source venv/bin/activate 

# Install dependencies:
   pip install Pipfile

# Run migrations:
    cd lib
    alembic upgrade head
# Seed dat on the project root
    python lib/seed.py

# Usage
 Run the CLI application: 
 python -m lib.cli

## Testing
 Run all tests:
pytest
  

## Database Schema

You can view the database schema diagram for the PetCareManager project here:

[PetCareManager Schema on dbdiagram.io](https://dbdiagram.io/d/PetCare-Manager-683454406980ade2eb67f8c5)

## Demo Video

Watch a demo of the PetCareManager project in action:

[Demo Video ](https://drive.google.com/file/d/1F7eWi4ZghgsQ95DoMilsgt4UyH0koV39/view?usp=sharing)

## Author
Name: Dominic Kipkorir  
GitHub: [https://github.com/Harshpal01/petcare_manager](https://github.com/Harshpal01/petcare_manager)


