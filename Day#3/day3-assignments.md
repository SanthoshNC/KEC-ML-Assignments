## 1 Pick any one of the algorithm from the units 3 / 4 / 5
###  Enter the choosen algorithm : DECISION TREE
###  Create a docker image for the same and push the same to dockerhub.
###  Add the screenshots here
CODING:
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('Appointment.csv')

# Parse 'Date' into separate features
df['Date'] = pd.to_datetime(df['Date'])
df['year']  = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day']   = df['Date'].dt.day

# Define features (X) and target (y)
X = df[['year', 'month', 'day', 'PatientID']]
y = df['DoctorID']

# Train on the full dataset
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

# Predict on the same data
y_pred = clf.predict(X)
acc = accuracy_score(y, y_pred)

print(f'Decision Tree accuracy on full dataset: {acc:.3f}')



DOCKERFILE

FROM python:3.9-slim
RUN pip install pandas scikit-learn matplotlib
COPY . .
CMD ["python","appointments.py"]

![image](https://github.com/user-attachments/assets/bebebc4f-bcf7-47c1-94af-79f7064782c0)


![image](https://github.com/user-attachments/assets/2de4375a-6a59-4b5b-85f7-d76686deeb01)

