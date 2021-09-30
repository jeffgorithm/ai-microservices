
# Load the Iris dataset from scikit-lear
from sklearn.datasets import load_iris
iris = load_iris()

# Import pandas and separate features from the target variable
import pandas as pd
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = pd.Series(iris.target)
X = df.loc[:, :].drop('target', axis=1)
y = df.loc[:, 'target']

# Cluster the data
from sklearn.cluster import KMeans
import sys
k = int(sys.argv[1])
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)
print(kmeans.cluster_centers_)


