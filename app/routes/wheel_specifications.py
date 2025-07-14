from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.get("/api/forms/wheel-specifications", response_model=list[schemas.WheelSpecificationOut])
def get_all_specs(db: Session = Depends(database.get_db)):
    return crud.get_wheel_specifications(db)
