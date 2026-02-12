from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app import models
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/slots", tags=["Slots"])

@router.post("/")
def create_slot(
    start_time: datetime,
    end_time: datetime,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    if current_user.role != "DOCTOR":
        logger.warning("Non-doctor tried to create slot")
        raise HTTPException(status_code=403, detail="Only doctors can create slots")

    slot = models.AvailabilitySlot(
        doctor_id=current_user.id,
        start_time=start_time,
        end_time=end_time
    )

    db.add(slot)
    db.commit()

    logger.info(f"Slot created by doctor {current_user.email}")

    return {"message": "Slot created successfully"}
