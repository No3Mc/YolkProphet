from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Split the data into training and test sets
train_data, test_data = train_test_split(data, test_size=0.2)

# Fit the model on the training data
model_fit = model.fit(train_data)

# Make predictions on the test data
predictions = model_fit.predict(test_data)

# Calculate the MAE, MSE, and R-squared for the predictions
mae = mean_absolute_error(test_data['Price'], predictions)
mse = mean_squared_error(test_data['Price'], predictions)
r2 = r2_score(test_data['Price'], predictions)

print("Mean Absolute Error: ", mae)
print("Mean Squared Error: ", mse)
print("R-squared: ", r2)
