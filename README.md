# FastAPI + MySQL Authentication System

A complete backend API built using FastAPI, MySQL, SQLAlchemy, JWT Authentication, and bcrypt password hashing. This project includes full authentication and authorization along with modules for Students, Courses, and Marks.

---

## Features

### Authentication
- User Registration
- User Login
- Password hashing using passlib[bcrypt]
- JWT Token generation (Access Token)
- Token verification for protected routes

### Authorization
Protected routes require the following header:

Authorization: Bearer <JWT_TOKEN>

### Student CRUD
- Add Student
- Get Students
- Update Student
- Delete Student

### Course Module
- Add Course
- Get Courses

### Marks Module
- Add Marks
- Get Student Marks

---

## Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python |
| Framework | FastAPI |
| Database | MySQL |
| ORM | SQLAlchemy |
| Authentication | JWT |
| Password Encryption | Bcrypt (Passlib) |
| API Testing | Swagger UI |

---

## How to Run the Project

### 1. Install required packages

pip install fastapi uvicorn sqlalchemy pymysql python-jose passlib[bcrypt]

### 2. Update your MySQL credentials

Edit `database.py`:

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/authdb"

### 3. Start the FastAPI server

uvicorn main:app --reload

### 4. Open API Documentation

Visit:

http://127.0.0.1:8000/docs

You can test:
- Register API
- Login API
- Protected routes
- CRUD operations

---

## Password Security

This system uses bcrypt hashing.

Example:

Input Password:
1234

Stored in Database:
$2b$12$TflKDMx2Qb3H...

Passwords cannot be reversed, ensuring secure authentication.

---

## Project Structure

fastapi_mysql_auth/
│── main.py                 # Application entry
│── database.py             # MySQL connection and engine setup
│── controllers/            # API route handlers
│── models/                 # SQLAlchemy models
│── schemas/                # Pydantic validation schemas
│── repositories/           # Data access layer
│── service/                # Business logic layer
│── utils/                  # JWT and hashing utilities
│── logs/                   # Logging files



