import logging  # ignore C0114

from fastapi import APIRouter

logger = logging.getLogger()

router = APIRouter()


@router.get("/heartbeat", description="Checks that the microservice is still up and running.")
async def heartbeat() -> dict:
    """Endpoint for checking the status of the microservice."""

    logger.info("Check that the microservice is up and running")
    return {}
