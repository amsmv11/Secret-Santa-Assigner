from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .utils_router import router as utils

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
