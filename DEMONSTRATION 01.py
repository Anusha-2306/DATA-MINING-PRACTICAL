#Aim: Implement K-Means Clustering Algorithm (Python Code using sklearn)
#K-Means clustering is a simple and popular machine learning algorithm
#used to group similar data points into clusters.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

# Step 1: Generate synthetic data or load your dataset
# Generate sample data
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=42)

# we use the K-Means algorithm to divide the data into 4 clusters
# Optionally standardize the dataset
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Visualize the data
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c='gray', marker='o', edgecolor='k')
plt.title("Data Distribution")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Step 3: Implement the K-Means algorithm
# Initialize and fit KMeans
kmeans = KMeans(n_clusters=4, random_state=42, n_init='auto') # Added n_init='auto' to suppress FutureWarning

kmeans.fit(X_scaled)

# Step 4: Extract Clustering results
cluster_labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

# Step 5: Visualize the clustered data
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=cluster_labels, cmap='viridis', marker='o', edgecolor='k')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

# Step 6: Evaluate clustering performance
# Calculate inertia (sum of squared distances to centroids)
print(f"Inertia: {kmeans.inertia_}")
