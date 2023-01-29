import pandas as pd

# Create an empty DataFrame to store historical egg prices
data = pd.DataFrame(columns=['Date', 'Price', 'Temperature','Location','Season','Supply_Demand','External_Factor'])

# Add dummy data to the DataFrame
data = data.append({'Date': '01-01-2021', 'Price': 2.5, 'Temperature': 20,'Location':'New York','Season':'Winter','Supply_Demand':'High','External_Factor':'None'}, ignore_index=True)
data = data.append({'Date': '01-02-2021', 'Price': 2.7, 'Temperature': 18,'Location':'New York','Season':'Winter','Supply_Demand':'High','External_Factor':'None'}, ignore_index=True)
data = data.append({'Date': '01-03-2021', 'Price': 2.9, 'Temperature': 15,'Location':'New York','Season':'Winter','Supply_Demand':'High','External_Factor':'None'}, ignore_index=True)
data = data.append({'Date': '01-04-2021', 'Price': 3.1, 'Temperature': 12,'Location':'New York','Season':'Winter','Supply_Demand':'High','External_Factor':'None'}, ignore_index=True)
data = data.append({'Date': '01-05-2021', 'Price': 3.0, 'Temperature': 10,'Location':'New York','Season':'Winter','Supply_Demand':'High','External_Factor':'None'}, ignore_index=True)

# Save the DataFrame to a CSV file
data.to_csv('egg_prices.csv', index=False)
