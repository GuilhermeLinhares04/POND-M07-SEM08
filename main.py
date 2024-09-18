from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime
import joblib
import pandas as pd

# Load the ARIMA model
arima_model = joblib.load('models/arima_model.pkl')

# Initialize the FastAPI app
app = FastAPI()

# Sample dataframe (normally you would load this from a file)
df = pd.read_csv('dados/Bitcoin_1Y_Normalizado.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])  # Ensure timestamp is datetime type
df.set_index('timestamp', inplace=True)

# Request model for the API
class PredictionRequest(BaseModel):
    start_date: str
    end_date: str

# Endpoint to get predictions for a given date range
@app.post("/predict/")
async def predict_price(request: PredictionRequest):
    # Parse the start and end dates
    try:
        start_date = datetime.fromisoformat(request.start_date)
        end_date = datetime.fromisoformat(request.end_date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

    # Remove timezone information from both the dataframe index and the date_range
    df.index = df.index.tz_localize(None)  # Make df.index timezone-naive
    current_last_date = df.index.max()

    # Generate the requested date range
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    # Calculate how many days are in the future compared to the current data
    days_in_future = max(0, (date_range[-1] - current_last_date).days)

    # Perform ARIMA forecast for requested days (both present and future)
    num_days = len(date_range)
    predictions = arima_model.forecast(steps=num_days)

    # Create a response with the dates and predicted prices
    prediction_data = {
        "predictions": [
            {"date": str(date), "predicted_close_price": float(price)}
            for date, price in zip(date_range, predictions)
        ]
    }
    return prediction_data

# To run the app use the command:
# uvicorn filename:app --reload
