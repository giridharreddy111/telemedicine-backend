from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app import models
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/")
def book_slot(
    slot_id: int,
    idempotency_key: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    if current_user.role != "PATIENT":
        logger.warning("Non-patient tried to book slot")
        raise HTTPException(status_code=403, detail="Only patients can book")

    existing_booking = db.query(models.Booking).filter(
        models.Booking.idempotency_key == idempotency_key
    ).first()

    if existing_booking:
        logger.info("Idempotent booking request detected")
        return {
            "message": "Already booked",
            "booking_id": existing_booking.id
        }

    slot = db.query(models.AvailabilitySlot).filter(
        models.AvailabilitySlot.id == slot_id,
        models.AvailabilitySlot.is_booked == False
    ).first()

    if not slot:
        logger.warning("Slot not available")
        raise HTTPException(status_code=400, detail="Slot not available")

    slot.is_booked = True

    booking = models.Booking(
        slot_id=slot_id,
        patient_id=current_user.id,
        idempotency_key=idempotency_key
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    logger.info(f"Slot {slot_id} booked by {current_user.email}")

    return {
        "message": "Slot booked successfully",
        "booking_id": booking.id
    }
