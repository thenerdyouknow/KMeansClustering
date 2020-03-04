import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy
import random

# random.seed(56)

FILE_PATH = "xclara.csv"

class K_Means_Clustering:
	
	def __init__(self,k_value,optimal_difference=0.001,maximum_iterations=1000):
		self.k_value = k_value
		self.optimal_difference = optimal_difference
		self.maximum_iterations = maximum_iterations

	def convert_to_list(self,df):
		return list(df.to_numpy())

	def calculate_euclidean_distance(self,p_list,q_list):
		squared_distance = 0
		
		assert len(p_list)==len(q_list),"The size of the co-oordinate lists don't match!"
		
		for i in range(len(p_list)):
			squared_distance += (p_list[i] - q_list[i])**2

		distance_between_two_points = math.sqrt(squared_distance)
		return distance_between_two_points

	def finding_min_element(self,list_to_use):
		min_value = 999999999999999999
		for i in range(len(list_to_use)):
			if(list_to_use[i]<min_value):
				min_value = list_to_use[i]
				min_value_index = i
		return min_value_index

	def finding_distance_from_centroids(self,point_to_use):
		all_distances = []
		for each_centroid in self.centroids:
			all_distances.append(self.calculate_euclidean_distance(point_to_use,self.centroids[each_centroid]))
		return all_distances

	def initialise_centroids(self,numpy_data):
		self.centroids = {}

		selected_centroids = random.sample(numpy_data,self.k_value)
		for i in range(len(selected_centroids)):
			self.centroids[i] = selected_centroids[i]

	def initialise_classes(self):
		self.classes = {}
		for j in range(self.k_value):
			self.classes[j] = []

	def classifying_points(self,numpy_data):
		for each_point in numpy_data:
			distance_from_centroids = self.finding_distance_from_centroids(each_point)
			closest_centroid = self.finding_min_element(distance_from_centroids)
			self.classes[closest_centroid].append(each_point)

	def computing_new_centroids(self):
		for each_class,all_points in self.classes.items():
			self.centroids[each_class] = numpy.average(all_points,axis=0)

	def checking_optimality(self,previous_copy):
		optimal_difference_flags = {}
		for each_centroid in self.centroids:
			optimal_difference_flags[each_centroid] = True

		for each_centroid in self.centroids:
			previous_position = previous_copy[each_centroid]
			current_copy = self.centroids[each_centroid]

			sum_of_difference = abs(numpy.sum((current_copy - previous_position)))

			if(sum_of_difference > self.optimal_difference):
				optimal_difference_flags[each_centroid] = False

		return optimal_difference_flags

	def fit(self,df):

		numpy_data = self.convert_to_list(df)
		self.initialise_centroids(numpy_data)		

		for i in range(self.maximum_iterations):
			self.initialise_classes()
			self.classifying_points(numpy_data)
			previous_copy = dict(self.centroids)
			self.computing_new_centroids()
			optimal_difference_flags = self.checking_optimality(previous_copy)
			if(all(value is True for key,value in optimal_difference_flags.items())):
				break

def plot_clusters(class_instance):
	colors =["r", "g", "c", "b","m","y"]*100

	for each_class in class_instance.classes:
		color = colors[each_class]
		for each_point in class_instance.classes[each_class]:
			plt.scatter(each_point[0],each_point[1],color=color,s=10)

	for centroids,values in class_instance.centroids.items():
		plt.scatter(values[0],values[1],s=150,color="k",marker="x")

	plt.show()


df = pd.read_csv(FILE_PATH)
km = K_Means_Clustering(3)
km.fit(df)
plot_clusters(km)
