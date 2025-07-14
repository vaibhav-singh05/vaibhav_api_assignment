from pydantic import BaseModel

class FormDataCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class FormDataResponse(FormDataCreate):
    id: int

    class Config:
        orm_mode = True

class BogieChecksheetCreate(BaseModel):
    inspector_name: str
    bogie_number: str
    remarks: str

class BogieChecksheetOut(BogieChecksheetCreate):
    id: int
    class Config:
        orm_mode = True

class WheelSpecificationCreate(BaseModel):
    wheel_type: str
    diameter: str
    material: str

class WheelSpecificationOut(WheelSpecificationCreate):
    id: int
    class Config:
        orm_mode = True
