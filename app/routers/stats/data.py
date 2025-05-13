from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List

from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.stock import AggregatedResult
from app.utils.stock_utils import get_aggregated_data

router = APIRouter()


@router.get("/strike_analysis", response_model=List[AggregatedResult])
def strike_analysis(
    period: str = Query(..., regex="^(daily|weekly|monthly)$"),
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    try:
        return get_aggregated_data(db, period, limit, offset)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
