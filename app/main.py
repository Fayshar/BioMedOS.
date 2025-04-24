from fastapi import FastAPI

app = FastAPI(
    title="BioMedOS Clinical AI",
    version="1.0.0",
    docs_url="/api/docs"
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
Initialize FastAPI app entry point
