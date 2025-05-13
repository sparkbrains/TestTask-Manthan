from datetime import timedelta

from sqlalchemy.orm import Session
from app.models import StockData
from sqlalchemy.sql import func

group_funcs = {
        "daily": func.date(StockData.date),
        "weekly": func.date_trunc("week", StockData.date),
        "monthly": func.date_trunc("month", StockData.date),
    }

def get_aggregated_data(db: Session, period: str, limit: int = 10, offset: int = 0):
    if period not in group_funcs:
        raise ValueError("Invalid aggregation. Must be one of: daily, weekly, monthly")

    group_func = group_funcs[period]

    query = (
        db.query(
            group_func.label("period_start"),
            func.avg(StockData.value).label("average_value")
        )
        .group_by("period_start")
        .order_by("period_start")
    )

    results = query.offset(offset).limit(limit).all()
    response = []

    for i, row in enumerate(results):
        if period == "daily":
            response.append({
                "label": "daily",
                "date": str(row.period_start),
                "average_value": round(row.average_value, 2)
            })
        else:
            start_date = row.period_start.date()

            if period == "weekly":
                end_date = start_date + timedelta(days=6)
                label = f"week{i + 1 + offset}"
            else:
                next_month = (start_date.replace(day=28) + timedelta(days=4)).replace(day=1)
                end_date = next_month - timedelta(days=1)
                label = f"month{i + 1 + offset}"

            response.append({
                "label": label,
                "start_date": str(start_date),
                "end_date": str(end_date),
                "average_value": round(row.average_value, 2)
            })

    return response