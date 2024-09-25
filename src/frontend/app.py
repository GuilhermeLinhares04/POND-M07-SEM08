import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import matplotlib.pyplot as plt

# Load the ARIMA model
arima_model = joblib.load('../models/arima_model.pkl')

# Load the dataset
df = pd.read_csv('../data/Bitcoin_1Y_Normalizado.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])  # Also making sure timestamp is datetime type
df.set_index('timestamp', inplace=True)

# Remove timezone information from the dataframe index
df.index = df.index.tz_localize(None)

st.title('Asset Price Prediction Dashboard')

# Input: date range for prediction
st.header("Make Predictions")
start_date = st.date_input("Start Date", min_value=df.index.min().date())
end_date = st.date_input("End Date", min_value=start_date)

# Convert start_date and end_date to datetime
start_date = datetime.combine(start_date, datetime.min.time())
end_date = datetime.combine(end_date, datetime.min.time())

# Calculate how many days into the future the user wants predictions
today = df.index.max()  # last available date in the dataset
num_days_future = (end_date - today).days if end_date > today else 0
num_days = (end_date - start_date).days + 1  # including the start date

# If the user clicks the "Predict" button
if st.button('Predict'):
    # Generate predictions
    if num_days_future > 0:
        # If the prediction includes future dates
        future_dates = pd.date_range(start=today + pd.Timedelta(days=1), periods=num_days_future, freq='D')
        future_predictions = arima_model.forecast(steps=num_days_future)

        # Create a DataFrame for future predictions
        future_df = pd.DataFrame({
            "Date": future_dates,
            "Predicted Price": future_predictions
        })

        # Select actual data until today and rename columns to avoid duplicates
        actual_data = df['close'][start_date:today].reset_index().rename(columns={"timestamp": "Date", "close": "Actual Price"})

        # Merge actual data with future predictions
        prediction_data = pd.concat([actual_data, future_df], ignore_index=True)

    else:
        # If the prediction is only within the dataset range
        prediction_data = pd.DataFrame({
            "Date": pd.date_range(start=start_date, end=end_date, freq='D'),
            "Predicted Price": arima_model.forecast(steps=num_days)
        })

    # Display predictions
    st.subheader(f"Predictions from {start_date.date()} to {end_date.date()}")
    st.write(prediction_data)

    # Plot the actual vs predicted prices
    st.subheader("Actual vs Predicted Prices")
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the actual data
    ax.plot(df.index, df['close'], label='Actual Prices')

    if num_days_future > 0:
        # Plot future predictions
        ax.plot(future_df['Date'], future_df['Predicted Price'], label='Future Predictions', color='red')
    else:
        # Plot predictions within the dataset range
        ax.plot(prediction_data['Date'], prediction_data['Predicted Price'], label='Predicted Prices', color='red')

    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(fig)

    # Analyzing the best date to buy/sell
    st.subheader("Recommendations for Buy/Sell")
    min_price_date = prediction_data.loc[prediction_data['Predicted Price'].idxmin()]['Date']
    max_price_date = prediction_data.loc[prediction_data['Predicted Price'].idxmax()]['Date']

    st.write(f"📉 Best date to **BUY**: {min_price_date.date()} (Lowest predicted price)")
    st.write(f"📈 Best date to **SELL**: {max_price_date.date()} (Highest predicted price)")
