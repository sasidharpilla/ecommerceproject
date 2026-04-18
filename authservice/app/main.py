from fastapi import FastAPI
from app.database import engine, Base
from app.models import user
from app.routes import auth

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])


@app.get("/")
def home():
    return {"message": "Auth Service Running"}