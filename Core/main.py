import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

# Read in the dataset containing historical egg prices
data = pd.read_csv('egg_prices.csv')

# Ask user for current price, date and temperature
current_price = input("Enter the current egg price: ")
current_date = input("Enter the current date (mm-dd-yyyy): ")
current_temp = input("Enter the current temperature: ")

# Append the current data to the historical data
data = data.append({'Price': current_price, 'Date': current_date, 'Temperature': current_temp}, ignore_index=True)

# Fit the ARIMA model to the data
model = ARIMA(data['Price'], order=(1,1,1))
model_fit = model.fit()

# Ask user for number of days to forecast
days_to_forecast = int(input("Enter the number of days to forecast: "))

# Make predictions for the next 7 days
predictions = model_fit.forecast(steps=days_to_forecast)[0]

# Create a new DataFrame to store the predictions
predictions_df = pd.DataFrame({'Date': [current_date + ' ' + i for i in range(1, days_to_forecast+1)], 'Price': predictions,'Temperature':current_temp})

# Save the predictions DataFrame to a CSV file
predictions_df.to_csv('egg_price_predictions.csv', index=False)
