import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
exam_scores = np.array([50, 55, 65, 70, 75, 80, 85, 90, 95, 100])

# Create and train the model
model = LinearRegression()
model.fit(hours_studied, exam_scores)

# Regression coefficients
intercept = model.intercept_
slope = model.coef_[0]

# Predicted scores
predicted_scores = model.predict(hours_studied)

# Plotting the results
plt.scatter(hours_studied, exam_scores, color='blue', label='Actual scores')
plt.plot(hours_studied, predicted_scores, color='red', label='Regression line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()

print(f"Intercept (beta_0): {intercept}")
print(f"Slope (beta_1): {slope}")
