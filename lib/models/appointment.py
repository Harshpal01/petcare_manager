from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from lib.models.base import Base
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
