from sqlalchemy import Column, Integer, String
from .database import Base

class FormData(Base):
    __tablename__ = "formdata"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"
    id = Column(Integer, primary_key=True, index=True)
    inspector_name = Column(String)
    bogie_number = Column(String)
    remarks = Column(String)

class WheelSpecification(Base):
    __tablename__ = "wheel_specification"
    id = Column(Integer, primary_key=True, index=True)
    wheel_type = Column(String)
    diameter = Column(String)
    material = Column(String)
