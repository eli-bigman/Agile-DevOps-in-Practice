from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="Health Check API",
    description="A simple API to monitor system health.",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    """
    Basic health check endpoint.
    Returns 200 OK with status and timestamp.
    """
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
