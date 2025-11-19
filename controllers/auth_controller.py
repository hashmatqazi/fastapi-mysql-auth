from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import HTTPBearer
from utils.jwt_handler import create_access_token, verify_token
from entities.student import Student

from database import SessionLocal

router = APIRouter(prefix="/auth", tags=["Auth"])

security = HTTPBearer()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    db = SessionLocal()
    user = db.query(Student).filter(Student.email == data.email).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email")
    
    import bcrypt
    if not bcrypt.checkpw(data.password.encode(), user.password.encode()):
          raise HTTPException(status_code=401, detail="Invalid password")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

# token verify dependency for protected routes
def get_current_user(token = Depends(security)):
    return verify_token(token.credentials)
