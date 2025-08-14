from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import Base, engine
from . import models
from .routers import student, admin

app = FastAPI(title="AI Assessment Backend", version="0.1.0")
Base.metadata.create_all(bind=engine)
app.add_middleware(CORSMiddleware, allow_origins=[settings.CORS_ORIGINS], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(admin.router)
app.include_router(student.router)
@app.get("/health")
def health(): return {"status": "ok"}
