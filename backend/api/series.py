from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from backend.db.session import get_db


router = APIRouter(tags=["series"])


@router.post("/search")
def search_groups(db: Session = Depends(get_db)):
    return {"Message": "Hello"}