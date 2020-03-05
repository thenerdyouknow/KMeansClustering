from sklearn.datasets import make_blobs
import csv

#create cluster blobs that are 2 dimensional, have 4 clusters, and are 10,000 points.
#the datapoints are equally distributed between the 4 clusters
X, y = make_blobs(n_samples=10000, centers=4, n_features=2)

with open('dummy_dataset.csv','w') as open_file:
	csv_writer = csv.writer(open_file)
	csv_writer.writerow(['X','Y','Cluster'])
	for i in range(len(X)):
		#append the cluster label to the coordinate and then write it to the csv
		new_Xi = list(X[i])
		new_Xi.append(y[i])
		csv_writer.writerow(new_Xi)