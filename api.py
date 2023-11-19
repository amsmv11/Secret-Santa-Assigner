import uvicorn

from src.api.setup_logging import setup_logging

setup_logging(path="logging.yaml")

# Initialize the FastAPI application
if __name__ == "__main__":
    uvicorn.run("api:app", port=8000, host="0.0.0.0", reload=True)
