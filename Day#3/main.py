import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("./diabetes_prediction_dataset.csv")

# Convert string columns to numeric using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['gender', 'smoking_history'], drop_first=True)

# Split into features and target
X = df_encoded.drop("diabetes", axis=1)
y = df_encoded["diabetes"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)
