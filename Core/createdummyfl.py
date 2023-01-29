import pandas as pd

# Create an empty DataFrame to store historical egg prices
data = pd.DataFrame(columns=['Date', 'Price', 'Temperature','Location','Season','Supply_Demand','External_Factor'])

# Add the current date, price, and temperature to the DataFrame
data = data.append({'Date': '01-01-2021', 'Price': 2.5, 'Temperature': 20,'Location':'New York','Season':'Winter','Supply_Demand':'High','External_Factor':'None'}, ignore_index=True)

# One-hot encoding for seasons
data = pd.get_dummies(data, columns=['Season'])

# Save the DataFrame to a CSV file with dummy variables
data.to_csv('egg_prices_with_season.csv', index=False)
