from fastapi import FastAPI
from api.v1.routes.clinical import router as clinical_router

app.include_router(
    clinical_router,
    prefix="/api/v1/clinical",
)
