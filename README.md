## PetCareManager
PetCareManager is a CLI-based application designed to help users manage pet care data, including clinics, pets, appointments, and pet visits. It leverages a modular Python codebase with SQLAlchemy ORM and Alembic for database migrations.
## Features
1.Manage Clinics, Pets, Appointments, and Clinic Pet Visits

2.Robust input validation helpers for user-friendly CLI experience

3.Modular and extensible architecture using Python packages

4.SQLite database support with Alembic migrations for schema management

5.Easy to run and extend for further pet care management features

## Installation
Clone the repository:
git clone git@github.com:Harshpal01/petcare_manager.git
cd petcare_manager
# Create and activate a virtual environment (recommended): 
python -m venv venv
source venv/bin/activate 

# Install dependencies:
pipenv install
pipenv shell

# Usage
Run the CLI application: python -m lib.cli

## Project Structure

petcare_manager/
├── lib/
│   ├── cli.py               # Command-line interface entry point
│   ├── helpers.py           # Input validation helper functions
│   └── models/              # SQLAlchemy models (Clinic, Pet, Appointment, etc.)
├── db/
│   └── migrations/          # Alembic migration scripts
├── petcare.db               # SQLite database file
├── seed.py                  # Script to populate initial data (optional)
├── README.md                # This file
├── Pipfile / Pipfile.lock   # Dependency management files
└── test_clinic.py           # Sample test file

## Database
Uses SQLite (petcare.db) as default database

Alembic is configured for database migrations

To apply migrations: alembic upgrade head

## Database Schema

You can view the database schema diagram for the PetCareManager project here:

[PetCareManager Schema on dbdiagram.io](https://dbdiagram.io/d/PetCare-Manager-683454406980ade2eb67f8c5)

## Demo Video

Watch a demo of the PetCareManager project in action:

[Demo Video ](https://drive.google.com/file/d/1F7eWi4ZghgsQ95DoMilsgt4UyH0koV39/view?usp=sharing)

## Author
Name: Dominic Kipkorir  
GitHub: [https://github.com/Harshpal01/petcare_manager](https://github.com/Harshpal01/petcare_manager)


