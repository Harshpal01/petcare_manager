from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models.base import Base

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

    def __repr__(self):
        return f"<Pet(id={self.id}, name={self.name}, species={self.species}, age={self.age},breed={self.breed}, owner={self.owner_name})>"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be non-negative")
        self._age = value

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
