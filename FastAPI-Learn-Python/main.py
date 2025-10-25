from fastapi import FastAPI
from database import engine, Base
from crud import router as crud_router

app = FastAPI()

# create DB tables
Base.metadata.create_all(bind=engine)

app.include_router(crud_router, prefix='/todo', tags=["Crud Router"])
