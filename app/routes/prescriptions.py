from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app import models
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/prescriptions", tags=["Prescriptions"])

@router.post("/")
def create_prescription(
    consultation_id: int,
    medication: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    if current_user.role != "DOCTOR":
        logger.warning("Non-doctor tried to create prescription")
        raise HTTPException(status_code=403, detail="Only doctors can create prescription")

    consultation = db.query(models.Consultation).filter(
        models.Consultation.id == consultation_id
    ).first()

    if not consultation:
        logger.warning("Consultation not found")
        raise HTTPException(status_code=404, detail="Consultation not found")

    prescription = models.Prescription(
        consultation_id=consultation_id,
        medication=medication
    )

    db.add(prescription)
    db.commit()

    logger.info(f"Prescription created by doctor {current_user.email}")

    return {"message": "Prescription created successfully"}
