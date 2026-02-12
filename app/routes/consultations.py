from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app import models
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/consultations", tags=["Consultations"])

@router.post("/")
def create_consultation(
    booking_id: int,
    notes: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    if current_user.role != "DOCTOR":
        logger.warning("Non-doctor tried to create consultation")
        raise HTTPException(status_code=403, detail="Only doctors can create consultation")

    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()

    if not booking:
        logger.warning("Booking not found for consultation")
        raise HTTPException(status_code=404, detail="Booking not found")

    consultation = models.Consultation(
        booking_id=booking_id,
        notes=notes
    )

    db.add(consultation)
    db.commit()

    logger.info(f"Consultation created by doctor {current_user.email}")

    return {"message": "Consultation created successfully"}
