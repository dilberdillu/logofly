from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.logo import CreateLogo, ShowLogo
from typing import List
from db.models.user import User
from db.repository.logo import create_new_logo
from apis.v1.route_login import get_current_user


router = APIRouter()

@router.get("", response_model=List[ShowLogo])
def get_all_logos():
    return {"request": "hello"}
    
