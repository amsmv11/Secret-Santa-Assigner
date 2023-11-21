import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.group_router import router as group
from src.api.setup_logging import setup_logging
from src.api.user_router import router as user
from src.api.utils_router import router as utils

setup_logging(path="logging.yaml")

# Initialize the FastAPI application
if __name__ == "__main__":
    uvicorn.run("main:create_app", port=8000, host="0.0.0.0", reload=True)


def create_app() -> FastAPI:
    """Create a FastAPI app."""
    app = FastAPI(
        version="0.1.0",
        title="Blank FastAPI Microservice Template",
        description="Blank FastAPI Microservice Template",
        docs_url="/",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    responses = {
        200: {"description": "Request was successful."},
        400: {"description": "Request was unsuccessful. Client error has occurred."},
        500: {"description": "Request was unsuccessful. Server error has occurred. "},
    }

    app.include_router(utils, prefix="/utils", tags=["utils"], responses=responses)  # type: ignore
    app.include_router(
        group, prefix="/api/v0/{owner_username}/group", tags=["Groups"], responses=responses
    )  # type: ignore
    app.include_router(user, prefix="/api/v0/user", tags=["Users"], responses=responses)  # type: ignore

    return app
