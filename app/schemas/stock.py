from pydantic import BaseModel
from typing import Union, Literal


class DailyResult(BaseModel):
    label: Literal["daily"]
    date: str
    average_value: float


class PeriodResult(BaseModel):
    label: str
    start_date: str
    end_date: str
    average_value: float


AggregatedResult = Union[DailyResult, PeriodResult]