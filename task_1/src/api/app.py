from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.csv_routes import csv_router 


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(csv_router,tags=["csv"])