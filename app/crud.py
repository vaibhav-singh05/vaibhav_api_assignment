from sqlalchemy.orm import Session
from . import models, schemas

def create_formdata(db: Session, data: schemas.FormDataCreate):
    new_entry = models.FormData(**data.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def get_formdata_by_id(db: Session, form_id: int):
    return db.query(models.FormData).filter(models.FormData.id == form_id).first()

def create_bogie_checksheet(db: Session, data: schemas.BogieChecksheetCreate):
    new_entry = models.BogieChecksheet(**data.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def get_wheel_specifications(db: Session):
    return db.query(models.WheelSpecification).all()
