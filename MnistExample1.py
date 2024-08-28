import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Step 1: Load the MNIST dataset
mnist = fetch_openml('mnist_784', version=1)
X = mnist.data
y = mnist.target.astype(np.int64)

# Step 2: Prepare the dataset
# To make it a regression problem, let's predict the value of one pixel (e.g., pixel 350) using other pixels
pixel_to_predict = 350
X_regression = X.drop(columns=[pixel_to_predict])
y_regression = X[pixel_to_predict]

# Using a subset of data for quicker computation (e.g., first 1000 samples)
X_regression_sample = X_regression.iloc[:1000]
y_regression_sample = y_regression.iloc[:1000]

# Step 3: Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_regression_sample, y_regression_sample, test_size=0.2, random_state=42)

# Step 4: Perform Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Calculate R-squared using sklearn
r_squared = r2_score(y_test, y_pred)
print(f"R-squared: {r_squared}")

# Step 5: Using statsmodels to get p-values and R-squared
X_train_sm = sm.add_constant(X_train)  # Adding a constant for statsmodels
ols_model = sm.OLS(y_train, X_train_sm).fit()
print(ols_model.summary())