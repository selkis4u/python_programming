import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

data = load_iris()
X = data.data

km = KMeans(n_clusters=3, random_state=42, n_init=10)
km.fit(X)

labels = km.labels_
print("무리별 인원=",np.bincount(labels))
print("무리가 안 흩어진 정도 = %.2f" %km.inertia_)
print("무리 중심점")
print(np.round(km.cluster_centers_, 2))

for c in range(3):
    m = labels == c
    print("무리", c, "인원", m.sum(), np.bincount(data.target[m], minlength=3))