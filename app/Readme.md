# Telemedicine Backend – FastAPI

A production-style Telemedicine backend built using FastAPI and SQLAlchemy.

This backend system supports:

- Role-based authentication (Doctor / Patient)
- Doctor slot creation
- Patient slot booking (Idempotent)
- Consultation creation
- Prescription generation
- JWT authentication
- Logging and health monitoring
- Dockerized deployment

---

## 🚀 Tech Stack

- FastAPI
- SQLAlchemy ORM
- SQLite (Development)
- JWT Authentication
- Uvicorn
- Docker
- Python 3.11+

---

## 📌 Core API Flow

1. Register Doctor
2. Register Patient
3. Login Doctor
4. Create Slot
5. Login Patient
6. Book Slot (Idempotent)
7. Login Doctor
8. Create Consultation
9. Create Prescription

---

## 🔐 Role-Based Access Control

| Endpoint | Role Required |
|----------|--------------|
| Create Slot | DOCTOR |
| Book Slot | PATIENT |
| Create Consultation | DOCTOR |
| Create Prescription | DOCTOR |

---

## 🧪 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
