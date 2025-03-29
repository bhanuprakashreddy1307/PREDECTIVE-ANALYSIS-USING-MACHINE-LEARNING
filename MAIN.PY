import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Create Synthetic Data
np.random.seed(42)
n_samples = 100
X = np.random.rand(n_samples, 1) * 10  # Feature: Random numbers between 0 and 10
y = 2.5 * X + np.random.randn(n_samples, 1) * 2  # Target: Linear relation with noise

# Convert to DataFrame
data = pd.DataFrame(np.hstack((X, y)), columns=["Feature", "Target"])
print("Generated Data:\n", data.head())

# Step 2: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train a Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Make Predictions
y_pred = model.predict(X_test)

# Step 5: Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")

# Step 6: Visualize the Results
plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Predictive Analysis using Linear Regression')
plt.legend()
plt.show()
