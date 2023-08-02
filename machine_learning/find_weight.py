import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Install required libraries (if not already installed)
# pip install numpy pandas scikit-learn

# Step 2: Gather the data
# Let's assume you have a CSV file named "data.csv" with two columns: "Height" and "Weight".

# Step 3: Load and preprocess the data
data = pd.read_csv("data.csv")

# Split the data into features (X) and target (y)
X = data[["Height"]]
y = data["Weight"]

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features to have zero mean and unit variance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 4: Train the model
# Create the Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Step 5: Evaluate the model
# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Step 6: Make predictions
# Function to predict weight from height
def predict_weight(height):
    height = scaler.transform([[height]])
    weight = model.predict(height)
    return weight[0]

# Example usage:
height_input = 175  # Replace this with the height of the object you want to predict
predicted_weight = predict_weight(height_input)
print(f"Predicted weight for a height of {height_input} cm: {predicted_weight:.2f} kg")
