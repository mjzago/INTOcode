import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def kmeans_clustering(X, n_clusters, initial_centers=None, Y=None):
    if Y is None:  # Corrected "is not provided" to "is None"
        data = np.array(X).reshape(-1, 1)
    else:
        data = np.column_stack((X, Y))
    
    if initial_centers is None:
        kmeans = KMeans(n_clusters=n_clusters)
    else:
        if Y is not None:
            kmeans = KMeans(n_clusters=n_clusters, init=initial_centers)
        else:
            kmeans = KMeans(n_clusters=n_clusters, init=initial_centers)
    
    kmeans.fit(data)
    cluster_centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    plt.figure(figsize=(8, 6))
    if Y is not None:
        plt.scatter(X, Y, c=labels, cmap='rainbow', s=100)
        plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], color='black', marker='x', s=200)
    else:
        plt.scatter(X, [0] * len(X), c=labels, cmap='rainbow', s=100)
        plt.scatter(cluster_centers, [0] * n_clusters, color='black', marker='x', s=200)
    
    plt.title(f'K-Means Clustering (K={n_clusters})')
    plt.xlabel('X-axis')
    if Y is not None:
        plt.ylabel('Y-axis')
    plt.show()

