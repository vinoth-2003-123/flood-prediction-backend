"""FastAPI application for the flood prediction decision-support backend."""

import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.schemas.prediction import PredictionRequest, PredictionResponse
from backend.services.prediction_service import process_prediction


logger = logging.getLogger(__name__)

app = FastAPI(
    title="Flood Prediction API",
    description="API for assessing supplied water-level predictions.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Status"])
def read_root() -> dict[str, str]:
    """Report that the Flood Prediction API is running."""
    return {"message": "Flood Prediction API is running."}


@app.get("/health", tags=["Status"])
def read_health() -> dict[str, str]:
    """Return the current API health status."""
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
def predict(request: PredictionRequest) -> PredictionResponse:
    """Assess an ML-supplied water-level prediction."""
    try:
        return process_prediction(request)
    except Exception as error:
        logger.exception("Failed to process prediction request")
        raise HTTPException(
            status_code=500,
            detail="Prediction could not be processed.",
        ) from error