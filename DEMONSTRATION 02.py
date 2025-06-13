#Aim: Implement Naïve Bayes Classifier for Text Classification (Python Code using sklearn).

# Import necessary libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample dataset
text = [
    "This is good",      # Positive
    "This is awesome",   # Positive
    "I hate this",       # Negative
    "This is terrible",  # Negative
    "This is great",     # Positive
    "This is worst"      # Negative
]

labels = ['positive', 'positive', 'negative', 'negative', 'positive', 'negative']

# Vectorize the text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text)

# Split data for training and test
X_train = X[:4]  # First 4 samples for training
y_train = labels[:4]

X_test = X[4:]   # Last 2 samples for testing
y_test = labels[4:]

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Predict the classes
y_pred = classifier.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("True Labels:", y_test)
print("Predicted Labels:", list(y_pred))
