# models.py

from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship, validates
from lib.base import Base

# Pet Model 
class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String, nullable=True)
    _age = Column("age", Integer, nullable=False)
    owner_name = Column(String, nullable=False)

    appointments = relationship("Appointment", back_populates="pet", cascade="all, delete-orphan")
    visits = relationship("ClinicPetVisit", back_populates="pet", cascade="all, delete-orphan")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be non-negative")
        self._age = value

    def __repr__(self):
        return f"<Pet(id={self.id}, name={self.name}, species={self.species}, age={self.age}, breed={self.breed}, owner={self.owner_name})>"

    def save(self, session):
        session.add(self)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id_):
        return session.query(cls).filter_by(id=id_).first()

    @classmethod
    def find_by_attribute(cls, session, attr_name, value):
        if not hasattr(cls, attr_name):
            return []
        return session.query(cls).filter(getattr(cls, attr_name) == value).all()

# Clinic Model
class Clinic(Base):
    __tablename__ = "clinics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    visits = relationship("ClinicPetVisit", back_populates="clinic", cascade="all, delete-orphan")
    appointments = relationship("Appointment", back_populates="clinic", cascade="all, delete-orphan")

    @validates('phone')
    def validate_phone(self, key, value):
        if not value or len(value) < 7:
            raise ValueError("Phone number must be at least 7 characters")
        return value

    def __repr__(self):
        return f"<Clinic(id={self.id}, name={self.name}, address={self.address}, phone={self.phone})>"

    def save(self, session):
        session.add(self)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id_):
        return session.query(cls).filter_by(id=id_).first()

    @classmethod
    def find_by_attribute(cls, session, attr_name, value):
        if not hasattr(cls, attr_name):
            return []
        return session.query(cls).filter(getattr(cls, attr_name) == value).all()

# Appointment Model
class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    clinic_id = Column(Integer, ForeignKey('clinics.id'))
    appointment_time = Column(DateTime)
    reason = Column(String)

    pet = relationship("Pet", back_populates="appointments")
    clinic = relationship("Clinic", back_populates="appointments")

    def save(self, session):
        session.add(self)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id_):
        return session.query(cls).filter_by(id=id_).first()

    @classmethod
    def find_by_attribute(cls, session, attr_name, value):
        if not hasattr(cls, attr_name):
            return []
        return session.query(cls).filter(getattr(cls, attr_name) == value).all()

# ClinicPetVisit Model 
class ClinicPetVisit(Base):
    __tablename__ = 'clinic_pet_visits'

    id = Column(Integer, primary_key=True)
    visit_date = Column(Date)
    notes = Column(String)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    clinic_id = Column(Integer, ForeignKey('clinics.id'))

    pet = relationship("Pet", back_populates="visits")
    clinic = relationship("Clinic", back_populates="visits")

    def __repr__(self):
        return f"<ClinicPetVisit(id={self.id}, date={self.visit_date}, pet_id={self.pet_id}, clinic_id={self.clinic_id})>"

    def save(self, session):
        session.add(self)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_attribute(cls, session, attr_name, value):
        if not hasattr(cls, attr_name):
            raise AttributeError(f"{cls.__name__} has no attribute '{attr_name}'")
        return session.query(cls).filter(getattr(cls, attr_name) == value).all()
