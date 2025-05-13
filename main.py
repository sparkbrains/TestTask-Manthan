from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers.stats import router as stats_router

app = FastAPI(root_path="/test1")

Base.metadata.create_all(bind=engine)

app.include_router(stats_router)