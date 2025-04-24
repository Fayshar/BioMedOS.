from fastapi import FastAPI, Depends
from api.v1.routes import clinical

app = FastAPI(
    title="BioMedOS Clinical AI",
    version="3.0",
    docs_url="/api/docs",
    redoc_url=None
)

app.include_router(
    clinical.router,
    prefix="/api/v1/clinical"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to BioMedOS"}
