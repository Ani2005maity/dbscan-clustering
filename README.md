<<<<<<< HEAD
# DBSCAN Clustering Example

This project demonstrates the DBSCAN clustering algorithm using Python and Scikit-learn.

The dataset contains 8 points and clustering is performed using:

ε (epsilon) = 3.5  
MinPts = 3

## Dataset

| Point | X | Y |
|-----|---|---|
| S1 | 5 | 7 |
| S2 | 8 | 4 |
| S3 | 3 | 3 |
| S4 | 4 | 4 |
| S5 | 3 | 7 |
| S6 | 6 | 7 |
| S7 | 6 | 1 |
| S8 | 5 | 5 |

## Algorithm

DBSCAN groups points based on density.

Types of points:

Core Point  
Boundary Point  
Noise Point

## Requirements

Install dependencies:

pip install -r requirements.txt

## Run the Program

python dbscan_demo.py

## Output

The program:

1. Calculates clusters using DBSCAN
2. Displays cluster assignments
3. Plots clustered points using matplotlib

## Example Output

Clusters will be displayed graphically where:

Cluster points are colored differently  
Noise points appear in red

## Technologies Used

Python  
Scikit-learn  
Matplotlib  
NumPy
