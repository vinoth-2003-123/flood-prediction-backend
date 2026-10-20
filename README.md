# AI-Based Flood Prediction System

## Module

FastAPI Backend, Severity Classification and Decision Support System.

## Installation

Install the required packages:

python -m pip install -r requirements.txt

## Start the Backend

Run this command from the project root:

python -m uvicorn backend.main:app --reload

## API Documentation

http://127.0.0.1:8000/docs

## Prediction Endpoint

POST /predict

### Example Request

{
"station": "Demo_Station",
"predicted_water_level": 3.5
}

## Response Fields

- station
- predicted_water_level
- severity
- threshold_status
- recommended_action

## Integration

The LSTM module sends predicted water levels to the FastAPI backend.
The frontend displays the returned JSON response.

## Important

Demonstration thresholds are for testing only.
Verified official station-specific thresholds are required before operational flood decisions.
