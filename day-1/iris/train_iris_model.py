from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# Import the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train a k-Nearest Neighbour Classifier, with k = 11
model = KNeighborsClassifier(n_neighbors=11)
model.fit(X, y)
print(f"Final Score: {model.score(X, y)}")

# save the model using pickle
import pickle
f = 'model.sav'
pickle.dump(model, open(f, 'wb'))

# Import the model and use it to make predictions
loaded_model = pickle.load(open(f, 'rb'))
print(f"Loaded Model Score: {loaded_model.score(X, y)}")
