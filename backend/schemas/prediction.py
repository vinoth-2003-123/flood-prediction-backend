"""Pydantic schemas for prediction requests and responses."""

from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    """Input prediction supplied by the ML or prediction layer."""

    station: str = Field(min_length=1, description="Station identifier")
    predicted_water_level: float = Field(
        allow_inf_nan=False,
        description="Water level predicted by the ML or prediction layer",
    )


class PredictionResponse(BaseModel):
    """Severity assessment and recommendation for a prediction."""

    station: str
    predicted_water_level: float
    severity: str
    threshold_status: str
    recommended_action: str