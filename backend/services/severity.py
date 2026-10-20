"""Classify predicted water levels using configured station thresholds."""


THRESHOLD_DATA_UNAVAILABLE = "Threshold data unavailable"

# Add verified thresholds for each station. Each value maps a severity name
# to the minimum water level for that severity.
# TEST ONLY — NOT OFFICIAL FLOOD WARNING THRESHOLDS
STATION_THRESHOLDS: dict[str, dict[str, float]] = {
    "Demo_Station": {
        "Normal": 2.0,
        "Above Normal": 3.0,
        "Severe": 4.0,
        "Extreme": 5.0,
    }
}


def assess_severity(
    station: str,
    predicted_water_level: float,
) -> dict[str, str]:
    """Return the severity and threshold status for a station prediction."""
    thresholds = STATION_THRESHOLDS.get(station)
    if not thresholds:
        return {
            "severity": THRESHOLD_DATA_UNAVAILABLE,
            "threshold_status": THRESHOLD_DATA_UNAVAILABLE,
        }

    ordered_thresholds = sorted(thresholds.items(), key=lambda item: item[1])
    severity = "below_configured_thresholds"
    threshold_status = f"Below {ordered_thresholds[0][0]} threshold"

    for severity_name, threshold in ordered_thresholds:
        if predicted_water_level < threshold:
            break

        severity = severity_name
        threshold_status = f"At or above {severity_name} threshold"

    return {
        "severity": severity,
        "threshold_status": threshold_status,
    }