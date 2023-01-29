import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

# Read in the dataset containing historical egg prices
data = pd.read_csv('egg_prices.csv')

# Ask user for current price, date and temperature
current_price = input("Enter the current egg price: ")
current_date = input("Enter the current date (mm-dd-yyyy): ")
current_temp = input("Enter the current temperature: ")
current_location = input("Enter the current location: ")
current_season = input("Enter the current season (summer, fall, winter, spring): ")
current_supply_demand = input("Enter the current supply-demand ratio: ")
current_external_factor = input("Enter any other external factors(if any): ")

# Append the current data to the historical data
data = data.append({'Price': current_price, 'Date': current_date, 'Temperature': current_temp,
'Location':current_location,'Supply_Demand':current_supply_demand,
'External_Factor':current_external_factor}, ignore_index=True)

# Create one-hot encoded columns for the "Season" variable
data = pd.get_dummies(data, columns=["Season"])

# Create one-hot encoded columns for the "Supply_Demand" variable
data = pd.get_dummies(data, columns=["Supply_Demand"])

# Fit the ARIMA model to the data
model = ARIMA(data['Price'], exog=data[['Season_summer', 'Season_fall', 'Season_winter', 'Season_spring','Supply_Demand_High','Supply_Demand_Low','Supply_Demand_Normal']], order=(1,1,1))
model_fit = model.fit()

# Ask user for number of days to forecast
days_to_forecast = int(input("Enter the number of days to forecast: "))

# Make predictions for the next days
predictions = model_fit.forecast(steps=days_to_forecast, exog=data[['Season_summer', 'Season_fall', 'Season_winter', 'Season_spring','Supply_Demand_High','Supply_Demand_Low','Supply_Demand_Normal']].tail(days_to_forecast))[0]

# Create a new DataFrame to store the predictions
predictions_df = pd.DataFrame({'Date': [current_date + ' ' + str(i) for i in range(1, days_to_forecast+1)], 'Price': predictions,'Temperature':current_temp,'Location':current_location,'Season':current_season,'Supply_Demand':current_supply_demand,'External_Factor':current_external_factor})

# Append the predictions DataFrame to the original dataset
data = data.append(predictions_df, ignore_index=True)

# Save the combined DataFrame to a CSV file
data.to_csv('egg_prices.csv', index=False) # Change the file name to the existing file you want to save the data to

print("Predictions have been made and added to the historical data with season and supply-demand as predictor variables.")
