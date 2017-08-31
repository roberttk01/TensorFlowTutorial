import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11], [8, 2], [10, 2], [9, 3]])

# plt.scatter(X[:, 0], X[:, 1], s=150)
# plt.show()

colors = 10 * ['g', 'r', 'c', 'b', 'k']


class Mean_Shift:

    def __init__(self, radius=4):
        # radius starts out at 4 because we know that would work for our current dataset
        self.radius = radius



    def fit(self, data):
        # Mean Shift method:
        #   1) Make all datapoints centroids
        #   2) Take mean of all featuresets within centroid's radius, setting this mean as new centroid
        #   3) Repeat step #2 until convergence

        centroids = {}

        for i in range(len(data)):
            centroids[i] = data[i]

        while True:
            new_centroids = []
            for i in centroids:
                in_bandwidth = []
                centroid = centroids[i]
                for featureset in data:
                    if np.linalg.norm(featureset - centroid) < self.radius:
                        in_bandwidth.append(featureset)

                new_centroid = np.average(in_bandwidth, axis=0)
                new_centroids.append(tuple(new_centroid))

            uniques = sorted(list(set(new_centroids)))

            prev_centroids = dict(centroids)

            centroids = {}
            for i in range(len(uniques)):
                centroids[i] = np.array(uniques[i])

            optimized = True

            for i in centroids:
                if not np.array_equal(centroids[i], prev_centroids[i]):
                    optimized = False
                if not optimized:
                    break

            if optimized:
                break

        self.centroids = centroids



clf = Mean_Shift()
clf.fit(X)

centroids = clf.centroids

plt.scatter(X[:, 0], X[:, 1], s=75)

for c in centroids:
    plt.scatter(centroids[c][0], centroids[c][1], color='k', marker="*", s=100)

plt.show()

