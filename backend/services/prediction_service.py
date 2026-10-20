"""Combine severity assessment and decision support for a prediction."""

from backend.schemas.prediction import PredictionRequest, PredictionResponse
from backend.services.decision_support import get_recommendation
from backend.services.severity import assess_severity


def process_prediction(request: PredictionRequest) -> PredictionResponse:
    """Assess a supplied prediction and return its recommended action."""
    assessment = assess_severity(
        station=request.station,
        predicted_water_level=request.predicted_water_level,
    )
    severity = assessment["severity"]

    return PredictionResponse(
        station=request.station,
        predicted_water_level=request.predicted_water_level,
        severity=severity,
        threshold_status=assessment["threshold_status"],
        recommended_action=get_recommendation(severity),
    )