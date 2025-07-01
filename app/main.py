from fastapi import FastAPI
from api import auth, salary
from models.db import Base, engine

app = FastAPI()

# Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(salary.router, tags=["salary"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Salary Service"}
