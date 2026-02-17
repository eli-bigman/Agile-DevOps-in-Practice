import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from datetime import datetime, timezone
from src.utils.system_info import get_system_stats

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Health Check API",
    description="A simple API to monitor system health.",
    version="1.0.0"
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global error occurred: {exc}")
    return JSONResponse(
        status_code=503,
        content={
            "status": "error",
            "reason": str(exc),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    )

@app.get("/health")
def health_check():
    """
    Basic health check endpoint.
    Returns 200 OK with status and timestamp.
    """
    logger.info("Health check requested")
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.get("/health/details")
def health_details():
    """
    Detailed health check including system resources.
    Returns CPU and Memory usage.
    """
    logger.info("Detailed health check requested")
    try:
        stats = get_system_stats()
        return {
            "status": "ok",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "system": stats
        }
    except Exception as e:
        logger.error(f"Error fetching system stats: {e}")
        raise e # Let global handler catch it


