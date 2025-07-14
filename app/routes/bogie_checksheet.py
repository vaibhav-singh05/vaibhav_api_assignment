from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.post("/api/forms/bogie-checksheet", response_model=schemas.BogieChecksheetOut)
def submit_bogie_checksheet(data: schemas.BogieChecksheetCreate, db: Session = Depends(database.get_db)):
    return crud.create_bogie_checksheet(db, data)
