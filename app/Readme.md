# Telemedicine Backend - FastAPI

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Docker

---

## Features
- User Registration (Doctor / Patient)
- JWT Login
- Role-based access control
- Doctor can create slots
- Patient can book slots
- Doctor can create consultations
- Doctor can create prescriptions
- Audit logging

---

## Setup Instructions

### 1. Create virtual environment
python -m venv venv

### 2. Activate
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run server
uvicorn app.main:app --reload

OpenAPI available at:
http://localhost:8000/docs


---

## Docker Setup

Build image:
docker build -t telemedicine-app .

Run container:
docker run -p 8000:8000 telemedicine-app

---

## API Flow

1. Register doctor
2. Register patient
3. Login doctor
4. Create slot
5. Login patient
6. Book slot
7. Login doctor
8. Create consultation
9. Create prescription
