from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from backend.db.session import get_db
from backend.service.series_service import search, external_query
from backend.db.schma import SearchRequest


router = APIRouter(tags=["series"])


@router.post("/search")
def search_groups(request: SearchRequest, db: Session = Depends(get_db)):
    db_res = search(request.title, db)

    if db_res:
        return {"Message": db_res}

    series_data = external_query(request.title, db)

    return {"data": series_data}