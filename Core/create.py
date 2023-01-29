import pandas as pd

# Create an empty DataFrame to store historical egg prices
data = pd.DataFrame(columns=['Date', 'Price', 'Temperature'])

# Ask the user for the current date, price, and temperature
date = input("Enter the current date (mm-dd-yyyy): ")
price = float(input("Enter the current price: "))
temperature = float(input("Enter the current temperature: "))

# Add the current date, price, and temperature to the DataFrame
data = data.append({'Date': date, 'Price': price, 'Temperature': temperature}, ignore_index=True)

# Save the DataFrame to a CSV file
data.to_csv('egg_prices.csv', index=False)
