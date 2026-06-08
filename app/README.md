# Hospital Management System Backend
## Project Structure
app/
├── api/
│   ├── base.py
│   └── v1/
│       ├── route_user.py
│       ├── route_login.py
│       ├── route_patient.py
│       ├── route_doctor.py
│       ├── route_appointment.py
│       └── route_history.py
├── core/
│   ├── config.py
│   └── security.py
├── crud/
│   ├── crud_user.py
│   ├── crud_patient.py
│   ├── crud_doctor.py
│   ├── crud_appointment.py
│   └── crud_history.py
├── db/
│   ├── base.py
│   └── session.py
├── models/
│   ├── models_user.py
│   ├── models_patient.py
│   ├── models_doctor.py
│   ├── models_appointment.py
│   └── models_history.py
├── schemas/
│   ├── schemas_user.py
│   ├── schemas_patient.py
│   ├── schemas_doctor.py
│   ├── schemas_appointment.py
│   └── schemas_history.py
└── main.py
## Features
- User Registration
- User Login
- JWT Token Authentication
- Patient Management
- Doctor Management
- Appointment Management
- Patient Medical History
- Doctor can view appointments
- Doctor can assign medicines and dosage time
- Patient and doctor can view patient history
## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite / MySQL
- JWT
- Passlib bcrypt
- Swagger UI
# API Flow
Register User
↓
Login User
↓
Get JWT Token
↓
Authorize in Swagger
↓
Create Doctor
↓
Create Patient
↓
Book Appointment
↓
Doctor Views Appointments
↓
Doctor Adds Patient History
↓
Patient Views History
# Modules

## 1. Authentication Module

### Purpose
Handles user registration, login, and JWT token generation.

### Features
- User Registration
- User Login
- Password Hashing
- JWT Token Generation
- JWT Token Validation
## 2. Patient Management Module

### Purpose
Manages patient information.

### Features
- Create Patient
- View Patient Details
- Update Patient Information
- Delete Patient
- View All Patients

### Patient Information
- Name
- Age
- Gender
- Disease
- Address
- Phone Number
## 3. Doctor Management Module

### Purpose
Manages doctor records.

### Features
- Create Doctor
- View Doctor Details
- Update Doctor Information
- Delete Doctor
- View All Doctors

### Doctor Information
- Name
- Age
- Gender
- Specialization
- Experience
- Address
- Phone Number
## 4. Appointment Management Module

### Purpose
Handles scheduling and management of appointments.

### Features
- Create Appointment
- View Appointments
- Update Appointment
- Cancel Appointment
- Doctor Appointment Tracking
- Patient Appointment Tracking

### Appointment Information
- Patient
- Doctor
- Date
- Time
- Status
## 5. Patient History Module

### Purpose
Maintains medical history records.

### Features
- Add Medical History
- View Medical History
- Doctor Notes
- Medicine Tracking
- Follow-up Records

### History Information
- Disease
- Medicines
- Dosage Time
- Doctor Notes
- Next Visit Date
## 6. Database Module

### Purpose
Handles database connectivity and table creation.

### Features
- Database Connection
- Session Management
- Table Registration
## 7. Security Module

### Purpose
Provides authentication and authorization services.

### Features
- Password Hashing
- Password Verification
- JWT Token Creation
- Token Validation
- Protected API Access
## 8. API Documentation Module

### Purpose
Provides interactive API testing and documentation.

### Features
- Swagger UI
- API Testing
- Request Validation
- Response Inspection
