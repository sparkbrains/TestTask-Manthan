from sqlalchemy import Column, Integer, Float, Date
from .database import Base

class StockData(Base):
    __tablename__ = "stock_data"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
