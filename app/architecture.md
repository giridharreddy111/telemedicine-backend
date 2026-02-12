# Telemedicine Backend Architecture

## 1. Overview

This project is a role-based Telemedicine Backend built using:

- FastAPI
- SQLAlchemy ORM
- SQLite (development)
- JWT Authentication
- Docker support

The system supports two roles:
- DOCTOR
- PATIENT

---

## 2. High-Level Architecture

Client (Swagger / Frontend)
        ↓
FastAPI Application
        ↓
Routers (Users, Slots, Bookings, Consultations, Prescriptions)
        ↓
Service Layer (Business Logic inside routes)
        ↓
SQLAlchemy ORM
        ↓
Database (SQLite / PostgreSQL ready)

---

## 3. Components

### 1️⃣ Authentication Layer
- JWT-based authentication
- OAuth2PasswordBearer
- Role-based access control

### 2️⃣ User Management
- Register user (Doctor / Patient)
- Login and receive JWT token

### 3️⃣ Slot Management
- Doctor creates availability slots
- Slot has start_time, end_time
- Slot marked as booked when reserved

### 4️⃣ Booking Management
- Patient books available slot
- Idempotency key prevents duplicate bookings

### 5️⃣ Consultation Management
- Only doctors can create consultation
- Linked to booking

### 6️⃣ Prescription Management
- Only doctors can create prescription
- Linked to consultation

---

## 4. Database Design

Entities:

- User
- AvailabilitySlot
- Booking
- Consultation
- Prescription
- AuditLog

Relationships:

User (Doctor) → AvailabilitySlot  
User (Patient) → Booking  
Booking → Consultation  
Consultation → Prescription  

---

## 5. Logging

- Python logging module used
- Logs important actions
- Helps debugging and monitoring

---

## 6. Scaling Design (Production Ready)

In production:

- Replace SQLite with PostgreSQL
- Use Docker container
- Run with Gunicorn + Uvicorn workers
- Add Redis for caching
- Use load balancer for horizontal scaling
- Use database indexing for performance

---

## 7. Security Design

- Password hashing
- JWT token expiration
- Role-based access control
- Protected endpoints
- Input validation via Pydantic
