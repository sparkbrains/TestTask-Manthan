from app.database import SessionLocal, engine
from app.models import Base, StockData
from datetime import date, timedelta
import random

Base.metadata.create_all(bind=engine)

db = SessionLocal()

start_date = date.today() - timedelta(days=59)

for i in range(60):
    current_date = start_date + timedelta(days=i)
    entries_for_day = random.randint(1, 4)

    for _ in range(entries_for_day):
        value = round(random.uniform(1500, 2600), 2)
        db.add(StockData(value=value, date=current_date))

db.commit()
db.close()
print("Seeded 60 days of data with multiple values per day.")