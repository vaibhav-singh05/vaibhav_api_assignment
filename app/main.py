from fastapi import FastAPI
from app.routes import bogie_checksheet, wheel_specifications
from app import models, database

app = FastAPI(title="KPA Form API Assignment")

models.Base.metadata.create_all(bind=database.engine)
app.include_router(bogie_checksheet.router)
app.include_router(wheel_specifications.router)
