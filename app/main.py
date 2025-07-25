from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import bogie_checksheet, wheel_specifications
from app import models, database

app = FastAPI(title="KPA Form API Assignment")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=database.engine)
app.include_router(bogie_checksheet.router)
app.include_router(wheel_specifications.router)
