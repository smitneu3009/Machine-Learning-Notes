# Simple Linear Regression Equation Demonstration

## Data

We have the following data:

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

## Calculation of Simple Linear Regression Equation

### Step 1: Calculate the Means

First, calculate the mean of \( X \) and \( Y \):

\[ \bar{X} = \frac{1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10}{10} = 5.5 \]

\[ \bar{Y} = \frac{50 + 55 + 65 + 70 + 75 + 80 + 85 + 90 + 95 + 100}{10} = 76.5 \]

### Step 2: Calculate the Slope (\(\beta_1\))

The formula for the slope \(\beta_1\) is:

\[ \beta_1 = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sum (X_i - \bar{X})^2} \]

Calculate the numerator:

\[ \sum (X_i - \bar{X})(Y_i - \bar{Y}) = (-4.5)(-26.5) + (-3.5)(-21.5) + (-2.5)(-11.5) + (-1.5)(-6.5) + (-0.5)(-1.5) + (0.5)(3.5) + (1.5)(8.5) + (2.5)(13.5) + (3.5)(18.5) + (4.5)(23.5) \]

\[ = 119.25 + 75.25 + 28.75 + 9.75 + 0.75 + 1.75 + 12.75 + 33.75 + 64.75 + 105.75 = 452.5 \]

Calculate the denominator:

\[ \sum (X_i - \bar{X})^2 = 20.25 + 12.25 + 6.25 + 2.25 + 0.25 + 0.25 + 2.25 + 6.25 + 12.25 + 20.25 = 82.5 \]

\[ \beta_1 = \frac{452.5}{82.5} = 5.4848 \approx 5.5 \]

### Step 3: Calculate the Intercept (\(\beta_0\))

The formula for the intercept \(\beta_0\) is:

\[ \beta_0 = \bar{Y} - \beta_1 \bar{X} \]

\[ \beta_0 = 76.5 - 5.5 \times 5.5 \]

\[ \beta_0 = 76.5 - 30.25 = 46.25 \]

### Step 4: Form the Regression Equation

Using the calculated \(\beta_1\) and \(\beta_0\), the regression equation is:

\[ Y = 46.25 + 5.5X \]

### Step 5: Make Predictions

Now, let's make predictions:

- If a student studies for 6 hours:

\[ Y = 46.25 + 5.5 \times 6 = 46.25 + 33 = 79.25 \]

- If a student studies for 8 hours:

\[ Y = 46.25 + 5.5 \times 8 = 46.25 + 44 = 90.25 \]

This concludes the demonstration of calculating the simple linear regression equation and making predictions based on it.
