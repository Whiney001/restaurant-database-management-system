import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, LabelEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.neural_network import MLPRegressor

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, LabelEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.pipeline import Pipeline

# Load the dataset
df = pd.read_csv('C:/Users/Winnie/Downloads/traversal_cost_data (1).csv')


# Encode categorical features
categorical_columns = ['type_of_terrain', 'zone_classification', 'time_of_day']  # Replace with actual column names in your dataset
label_encoders = {col: LabelEncoder() for col in categorical_columns}
for col in categorical_columns:
    if col in df.columns:  # Check if column exists
        df[col] = label_encoders[col].fit_transform(df[col])
    else:
        print(f"Warning: Column '{col}' not found in the dataset.")

# Split the data into features (X) and target (y)
if 'traversal_cost' in df.columns:  # Ensure the target column exists
    X = df.drop(columns=['traversal_cost'])
    y = df['traversal_cost']
else:
    raise KeyError("The target column 'traversal_cost' is not found in the dataset.")

# Standardize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and testing sets (80-20)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# --- Linear Regression ---
# Train the linear regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Predict on the test set
y_pred_linear = linear_model.predict(X_test)

# Evaluate the model
mae_linear = mean_absolute_error(y_test, y_pred_linear)
mse_linear = mean_squared_error(y_test, y_pred_linear)
rmse_linear = np.sqrt(mse_linear)
print(f"Linear Regression - MAE: {mae_linear}, MSE: {mse_linear}, RMSE: {rmse_linear}")
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, LabelEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.neural_network import MLPRegressor

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, LabelEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.pipeline import Pipeline

# Load the dataset
df = pd.read_csv('C:/Users/Winnie/Downloads/traversal_cost_data (1).csv')


# Encode categorical features
categorical_columns = ['type_of_terrain', 'zone_classification', 'time_of_day']  # Replace with actual column names in your dataset
label_encoders = {col: LabelEncoder() for col in categorical_columns}
for col in categorical_columns:
    if col in df.columns:  # Check if column exists
        df[col] = label_encoders[col].fit_transform(df[col])
    else:
        print(f"Warning: Column '{col}' not found in the dataset.")

# Split the data into features (X) and target (y)
if 'traversal_cost' in df.columns:  # Ensure the target column exists
    X = df.drop(columns=['traversal_cost'])
    y = df['traversal_cost']
else:
    raise KeyError("The target column 'traversal_cost' is not found in the dataset.")

# Standardize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and testing sets (80-20)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# --- Linear Regression ---
# Train the linear regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Predict on the test set
y_pred_linear = linear_model.predict(X_test)

# Evaluate the model
mae_linear = mean_absolute_error(y_test, y_pred_linear)
mse_linear = mean_squared_error(y_test, y_pred_linear)
rmse_linear = np.sqrt(mse_linear)
print(f"Linear Regression - MAE: {mae_linear}, MSE: {mse_linear}, RMSE: {rmse_linear}")

# --- Polynomial Regression ---
# Train a polynomial regression model (degree 4)
poly_pipeline = Pipeline([
    ('poly_features', PolynomialFeatures(degree=4)),
    ('linear_model', LinearRegression())
])
poly_pipeline.fit(X_train, y_train)

# Predict on the test set
y_pred_poly = poly_pipeline.predict(X_test)

# Evaluate the model
mae_poly = mean_absolute_error(y_test, y_pred_poly)
mse_poly = mean_squared_error(y_test, y_pred_poly)
rmse_poly = np.sqrt(mse_poly)
print(f"Polynomial Regression - MAE: {mae_poly}, MSE: {mse_poly}, RMSE: {rmse_poly}")

# Train a polynomial regression model (degree 4)

poly_pipeline.fit(X_train, y_train)

# Predict on the test set
y_pred_poly = poly_pipeline.predict(X_test)

# Evaluate the model
mae_poly = mean_absolute_error(y_test, y_pred_poly)
mse_poly = mean_squared_error(y_test, y_pred_poly)
rmse_poly = np.sqrt(mse_poly)
print(f"Polynomial Regression - MAE: {mae_poly}, MSE: {mse_poly}, RMSE: {rmse_poly}")

# --- Neural Network (MLP Regressor) ---
# Train the neural network model
nn_model = MLPRegressor(
    hidden_layer_sizes=(128, 64),  # Two hidden layers with 128 and 64 neurons
    activation='relu',            # ReLU activation function
    solver='adam',                # Optimizer
    learning_rate_init=0.001,     # Learning rate
    max_iter=500,                 # Maximum iterations
    random_state=42
)
nn_model.fit(X_train, y_train)

# Predict on the test set
y_pred_nn = nn_model.predict(X_test)

# Evaluate the model
mae_nn = mean_absolute_error(y_test, y_pred_nn)
mse_nn = mean_squared_error(y_test, y_pred_nn)
rmse_nn = np.sqrt(mse_nn)
print(f"Neural Network - MAE: {mae_nn}, MSE: {mse_nn}, RMSE: {rmse_nn}")







