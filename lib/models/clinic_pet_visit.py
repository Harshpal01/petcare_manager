# lib/models/clinic_pet_visit.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class ClinicPetVisit(Base):
    __tablename__ = 'clinic_pet_visits'

    id = Column(Integer, primary_key=True)
    visit_date = Column(Date)
    notes = Column(String)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    clinic_id = Column(Integer, ForeignKey('clinics.id'))

    pet = relationship("Pet", back_populates="visits")
    clinic = relationship("Clinic", back_populates="visits")

    def save(self, session):
        session.add(self)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"<ClinicPetVisit(id={self.id}, date={self.visit_date}, pet_id={self.pet_id}, clinic_id={self.clinic_id})>"
    @classmethod
    def find_by_attribute(cls, session, attr_name, value):
        if not hasattr(cls, attr_name):
            raise AttributeError(f"{cls.__name__} has no attribute '{attr_name}'")
        return session.query(cls).filter(getattr(cls, attr_name) == value).all()
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()