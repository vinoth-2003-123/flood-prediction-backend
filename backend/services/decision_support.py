"""Provide system recommendations for configured severity levels."""


RECOMMENDATIONS: dict[str, str] = {
    "Normal": "Continue routine monitoring.",
    "Above Normal": (
        "Increase monitoring frequency and closely observe the predicted "
        "water level."
    ),
    "Severe": (
        "Notify the responsible monitoring team and follow the configured "
        "flood-management procedure."
    ),
    "Extreme": (
        "Follow the official emergency and flood-management procedure "
        "immediately."
    ),
    "Threshold data unavailable": (
        "Decision support unavailable because flood thresholds are not "
        "configured."
    ),
}


def get_recommendation(severity: str) -> str:
    """Return the recommendation for a severity label.

    Pass the ``severity`` value from the result of
    ``services.severity.assess_severity``.
    """
    return RECOMMENDATIONS.get(
        severity,
        "No recommendation is configured for this severity.",
    )