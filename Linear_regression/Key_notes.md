# Simple Linear Regression

## Why Simple Linear Regression is Used

Simple linear regression is used to:

1. **Predict Outcomes**: It allows us to make predictions about the dependent variable based on the value of the independent variable.
2. **Understand Relationships**: It helps us understand the relationship between two variables—specifically, how the change in one variable affects the other.
3. **Quantify Relationships**: It provides a quantitative measure (slope) of the relationship between the two variables, helping us understand the strength and direction of the relationship.

## Example: Students and Hours Studied

Let's revisit the example of students' exam scores based on the number of hours they studied.

### Scenario

- **Dependent Variable (Y)**: Exam Score (the outcome we want to predict)
- **Independent Variable (X)**: Hours Studied (the predictor)

The goal is to see if there's a linear relationship between the number of hours studied and the exam score, and if so, use this relationship to predict exam scores.

### Data

Here is the data we have:

| Hours Studied (X) | Exam Score (Y) |
|-------------------|----------------|
| 1                 | 50             |
| 2                 | 55             |
| 3                 | 65             |
| 4                 | 70             |
| 5                 | 75             |
| 6                 | 80             |
| 7                 | 85             |
| 8                 | 90             |
| 9                 | 95             |
| 10                | 100            |

### Steps to Perform Simple Linear Regression

1. **Plot the Data**: Plot a scatter plot to visualize the data. This helps in seeing if there's a linear trend.
   - On the x-axis, we plot the hours studied.
   - On the y-axis, we plot the exam scores.

2. **Fit the Model**: Use simple linear regression to fit a line through the data points. The line is of the form:
   \[ Y = \beta_0 + \beta_1X \]
   - \(\beta_0\) (intercept): The predicted exam score when no hours are studied.
   - \(\beta_1\) (slope): The increase in the exam score for each additional hour studied.

3. **Make Predictions**: Use the fitted line to predict exam scores for different values of hours studied.

### Interpretation

- **Intercept (\(\beta_0\))**: This is the value of the exam score when the hours studied are zero. It gives us a baseline score.
- **Slope (\(\beta_1\))**: This indicates how much the exam score increases for each additional hour of study. For example, if the slope is 5, then for each extra hour studied, the exam score increases by 5 points.

## Summary

- **Usefulness**: Simple linear regression helps in predicting outcomes and understanding relationships between two variables.
- **Example**: The example of students and hours studied shows how studying more hours is associated with higher exam scores, and the model helps quantify this relationship.
