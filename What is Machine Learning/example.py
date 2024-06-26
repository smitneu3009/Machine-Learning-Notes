from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample data
emails = [
    "Win a free iPhone now!",
    "Meeting rescheduled to 3 PM",
    "Get cheap insurance",
    "Lunch at noon?",
    "Exclusive deal just for you!"
]
labels = [1, 0, 1, 0, 1]  # 1 = Spam, 0 = Not Spam

# Convert text data to feature vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Predict on a new email
new_email = ["Exclusive deal just for you!"]
new_email_vec = vectorizer.transform(new_email)
prediction = model.predict(new_email_vec)
print(f"Prediction for new email: {'Spam' if prediction[0] == 1 else 'Not Spam'}")
