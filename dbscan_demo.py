import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Dataset from the problem
points = np.array([
    [5,7],  # S1
    [8,4],  # S2
    [3,3],  # S3
    [4,4],  # S4
    [3,7],  # S5
    [6,7],  # S6
    [6,1],  # S7
    [5,5]   # S8
])

labels = ["S1","S2","S3","S4","S5","S6","S7","S8"]

# DBSCAN parameters
epsilon = 3.5
min_points = 3

# Run DBSCAN
model = DBSCAN(eps=epsilon, min_samples=min_points)
clusters = model.fit_predict(points)

print("Point  Coordinates   Cluster")
for i in range(len(points)):
    print(labels[i], points[i], clusters[i])

# Plot clusters
plt.figure(figsize=(6,6))

unique_clusters = set(clusters)

for cluster in unique_clusters:
    
    if cluster == -1:
        color = 'red'
        label = 'Noise'
    else:
        color = None
        label = f'Cluster {cluster}'
        
    cluster_points = points[clusters == cluster]
    
    plt.scatter(
        cluster_points[:,0],
        cluster_points[:,1],
        label=label,
        s=100
    )

# annotate points
for i, txt in enumerate(labels):
    plt.annotate(txt,(points[i][0],points[i][1]))

plt.title("DBSCAN Clustering (ε=3.5, MinPts=3)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

plt.show()