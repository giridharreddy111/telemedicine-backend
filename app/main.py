from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import users, slots, bookings, consultations, prescriptions
import logging

# Configure logging (ONLY here)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)
logger.info("Database tables created successfully")

# Include routers
app.include_router(users.router)
app.include_router(slots.router)
app.include_router(bookings.router)
app.include_router(consultations.router)
app.include_router(prescriptions.router)

@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {"message": "Telemedicine API running"}

@app.get("/health")
def health():
    logger.info("Health check endpoint accessed")
    return {"status": "healthy"}
