# Team Name : Yeet!
# Team Member 1 : Venkatesh Thapan
# Team Member 2 : Ishita Singhal
# Team Member 3 : Asiket Singh Dhillon

import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy
import random

random.seed(250)

FILE_PATH = "4_cluster_data.csv"

class K_Means_Clustering:
	
	def __init__(self,k_value,optimal_difference=0.001,maximum_iterations=1000):
		'''intialising the k number of clusters, the difference at which we stop iterating, and the maximum number of iterations'''
		self.k_value = k_value
		self.optimal_difference = optimal_difference
		self.maximum_iterations = maximum_iterations

	def convert_to_list(self,df):
		'''convert df to a numpy list'''
		return list(df.to_numpy())

	def calculate_euclidean_distance(self,p_list,q_list):
		'''calculate euclidean distance between two points'''
		squared_distance = 0
		#asserting that the length of both x and y cooordinates are the same, else exit the program
		assert len(p_list)==len(q_list),"The size of the co-oordinate lists don't match!"
		
		for i in range(len(p_list)):
			#formula to calculate euclidean distance
			squared_distance += (p_list[i] - q_list[i])**2

		distance_between_two_points = math.sqrt(squared_distance)
		return distance_between_two_points

	def finding_min_element(self,list_to_use):
		'''finding index of the minimum element in a list'''
		min_value = 999999999999999999
		for i in range(len(list_to_use)):
			if(list_to_use[i]<min_value):
				min_value = list_to_use[i]
				min_value_index = i
		return min_value_index

	def finding_distance_from_centroids(self,point_to_use):
		'''calculating distance of a point from all the centroids'''
		all_distances = []
		for each_centroid in self.centroids:
			all_distances.append(self.calculate_euclidean_distance(point_to_use,self.centroids[each_centroid]))
		return all_distances

	def initialise_centroids(self,numpy_data):
		'''initialising the centroids by randomly selecting k values from the datapoints'''
		self.centroids = {}

		selected_centroids = random.sample(numpy_data,self.k_value)
		for i in range(len(selected_centroids)):
			self.centroids[i] = selected_centroids[i]

	def initialise_classes(self):
		'''initialising lists for all the classes'''
		self.classes = {}
		for j in range(self.k_value):
			self.classes[j] = []

	def classifying_points(self,numpy_data):
		'''finding distance of a point from all the centroids, finding the closest centroid, and appending the point to the list of that centroid'''
		for each_point in numpy_data:
			distance_from_centroids = self.finding_distance_from_centroids(each_point)
			closest_centroid = self.finding_min_element(distance_from_centroids)
			self.classes[closest_centroid].append(each_point)

	def computing_new_centroids(self):
		'''computing new centroid coordinates by average the x and y coordinates of all the points belonging to that centroid'''
		for each_class,all_points in self.classes.items():
			self.centroids[each_class] = numpy.average(all_points,axis=0)

	def checking_optimality(self,previous_copy):
		'''checking if the position of the centroid has changed enough since the last iteration, if not then we're done with clustering'''
		optimal_difference_flags = {}
		for each_centroid in self.centroids:
			optimal_difference_flags[each_centroid] = True

		for each_centroid in self.centroids:
			previous_position = previous_copy[each_centroid]
			current_copy = self.centroids[each_centroid]

			#finding absolute difference between the previous coordinates and the current coordinates and them summing the coordinates
			sum_of_difference = abs(numpy.sum((current_copy - previous_position)))

			if(sum_of_difference > self.optimal_difference):
				optimal_difference_flags[each_centroid] = False

		return optimal_difference_flags

	def fit(self,df):
		''' the fit driver function to complete clustering'''
		numpy_data = self.convert_to_list(df)
		self.initialise_centroids(numpy_data)		

		for i in range(self.maximum_iterations):
			self.initialise_classes()
			self.classifying_points(numpy_data)
			previous_copy = dict(self.centroids)
			self.computing_new_centroids()
			optimal_difference_flags = self.checking_optimality(previous_copy)
			if(all(value is True for key,value in optimal_difference_flags.items())):
				#if all centroids haven't moved enough from the last position, then stop the clustering
				break

def plot_clusters(class_instance):
	'''plotting the clusters'''
	colors =["r", "g", "c", "b","m","y"]*100

	for each_class in class_instance.classes:
		color = colors[each_class]
		for each_point in class_instance.classes[each_class]:
			#plotting each point using the colour for that cluster
			plt.scatter(each_point[0],each_point[1],color=color,s=10)

	for centroids,values in class_instance.centroids.items():
		#marking the centroid for cluster
		plt.scatter(values[0],values[1],s=150,color="k",marker="x")

	plt.show()

def main():
	df = pd.read_csv(FILE_PATH)
	km = K_Means_Clustering(4)
	km.fit(df[['X','Y']])
	plot_clusters(km)

if __name__ == '__main__':
	main()