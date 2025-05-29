from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from lib.models.base import Base


class Clinic(Base):
    __tablename__ = "clinics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    visits = relationship("ClinicPetVisit", back_populates="clinic", cascade="all, delete-orphan")
    appointments = relationship("Appointment", back_populates="clinic", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Clinic(id={self.id}, name={self.name}, address={self.address}, phone={self.phone})>"

    @validates('phone')
    def validate_phone(self, key, value):
        if not value or len(value) < 7:
            raise ValueError("Phone number must be at least 7 characters")
        return value

    # CRUD helper methods
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
