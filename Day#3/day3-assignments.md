## 1 Pick any one of the algorithm from the units 3 / 4 / 5
###  Enter the choosen algorithm
from pandas import read_csv
from matplotlib import pyplot
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# 1. Load dataset
filename = "Iris.csv"
data = read_csv(filename)

# 2. Display shape & preview
print("Shape of the dataset:", data.shape)
print("First 20 rows:\n", data.head(20))

# 3. Plot & save histograms
data.hist()
pyplot.savefig("histograms.png")
pyplot.close()

# 4. Plot & save density plots
data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
pyplot.savefig("density_plots.png")
pyplot.close()

# 5. Prepare features/labels
array = data.values
X = array[:, 1:5]   # columns 1–4
Y = array[:, 5]     # column 5

# 6. Train/test split
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=test_size, random_state=seed
)

# 7. Define classifiers to run
models = {
    "logistic": LogisticRegression(max_iter=200, random_state=seed),
    "decision_tree": DecisionTreeClassifier(max_depth=3, random_state=seed),
    "knn": KNeighborsClassifier(n_neighbors=5),
    "random_forest": RandomForestClassifier(n_estimators=100, random_state=seed)
}

# 8. Train, evaluate, and save each
for name, model in models.items():
    model.fit(X_train, Y_train)
    accuracy = model.score(X_test, Y_test) * 100
    print(f"{name.replace('_', ' ').title()} Accuracy: {accuracy:.2f}%")
    joblib.dump(model, f"{name}_model.pkl")

###  Create a docker image for the same and push the same to dockerhub.
###  Add the screenshots here
![image](https://github.com/user-attachments/assets/addc9cb1-8868-4dc9-8981-9d326416acf8)

![image](https://github.com/user-attachments/assets/2532ceb3-7a6f-4326-81cf-4b892c1aef2d)
