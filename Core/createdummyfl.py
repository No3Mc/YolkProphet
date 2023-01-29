import pandas as pd

# Create an empty DataFrame to store historical egg prices
data = pd.DataFrame(columns=['Date', 'Price', 'Temperature','Location','Season','Supply_Demand','External_Factor'])

# Add the current date, price, and temperature to the DataFrame
data = data.append({'Date': '01-01-2021', 'Price': 2.5, 'Temperature': 20,'Location':'New York','Season':'Winter','Supply_Demand':'High','External_Factor':'None'}, ignore_index=True)

# Save the DataFrame to a CSV file
data.to_csv('egg_prices.csv', index=False)
