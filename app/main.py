from fastapi import FastAPI
from pydantic import BaseSettings
import uvicorn

class Settings(BaseSettings):
    APP_PORT: int
    RX_NORM_API_URL: str
    DRUG_SAFETY_API: str
    DATABASE_URL: str
    GOOGLE_CLOUD_CREDENTIALS: str

    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI(
    title="BioMedOS Clinical AI",
    version="1.0.0",
    docs_url="/api/docs"
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.APP_PORT)
